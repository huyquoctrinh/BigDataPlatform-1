from flask import Flask
from modules.utils.celery_init import celery_init_app

app = Flask(__name__)
app.config.from_mapping(
    CELERY=dict(
        broker_url="redis://localhost",
        result_backend="redis://localhost",
        task_ignore_result=True,
    ),
)
celery_app = celery_init_app(app)
worker.conf.result_backend = os.getenv(
    "CELERY_RESULT_BACKEND", "redis://localhost:6379"
)
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=int(os.getenv("REDIS_METRICS_DB", 5)),
    decode_responses=True
)

