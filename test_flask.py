from flask import Flask
from flask import request, jsonify
app = Flask(__name__)
# app.config.from_mapping(
#     CELERY=dict(
#         broker_url="redis://localhost:6379",
#         result_backend="redis://localhost",
#         task_ignore_result=True,
#     ),
# )

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["audio_file"]
    print(file.filename)
    print(request.form.get("id"))
    print(request.form.get("device"))
    print(request.form.get("db"))

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)
