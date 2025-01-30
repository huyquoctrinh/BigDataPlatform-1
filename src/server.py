from flask import Flask
from worker import celery
from utils.extract_meta_data import extract_metadata_from_request
from celery.result import AsyncResult
from flask import request, jsonify
import logging
import celery.states as states


logging.basicConfig(filename="./logs/app.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_file():
    results = extract_metadata_from_request(request)
    results_dict = results.to_dict()
    results_dict["file_tmp"] = "/tmp/" + request.files["audio_file"].filename
    request.files["audio_file"].save(results_dict["file_tmp"])
    metadata_update_results = celery.send_task(
        "tasks.update_metadata", 
        args=[results_dict]
    )
    upload_results = celery.send_task(
        "tasks.upload_file_to_minio", 
        args=[results_dict["file_tmp"]],
        kwargs={}
    )
    logging.info(f"Task ID: {results.id}")
    return jsonify({"status": "success", "task_id": results.id})

@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)

# @app.get("/result/<id>")
# def task_result(id: str) -> dict[str, object]:
#     result = AsyncResult(id)
#     return {
#         "ready": result.ready(),
#         "successful": result.successful(),
#         "value": result.result if result.ready() else None,
#     }

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)