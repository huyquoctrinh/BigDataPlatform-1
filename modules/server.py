from flask import Flask
from modules.workers.upload_file import upload_file_to_minio
from modules.workers.extract_data import extract_metadata
from celery.result import AsyncResult

app = Flask(__name__)
app.config.from_mapping(
    CELERY=dict(
        broker_url="redis://localhost:6379",
        result_backend="redis://localhost",
        task_ignore_result=True,
    ),
)

@app.post("/upload", methods=["POST"])
def upload_file():
    results = extract_metadata.delay(request)
    return jsonify({"status": "success", "task_id": results.id})

@app.get("/result/<id>")
def task_result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    return {
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)