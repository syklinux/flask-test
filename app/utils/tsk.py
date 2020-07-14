
from celery import Celery

from app.config.secure import CELERY_BROKER_URL,CELERY_RESULT_BACKEND

celery = Celery(__name__, broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task()
def test():
    print("okokokokok")


@celery.task(name="import_data")
def import_data():
    print('dsadasd')