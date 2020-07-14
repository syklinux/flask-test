
from datetime import timedelta

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:xxx@ip:3307/ticket_test"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '\xe4\xf5\xd7F\xf6\xb3kMr"\xa5\xff\t\xa1}\xb2\x00\xe0\x01\xf3\xd5\xce@6'

CELERY_BROKER_URL = 'redis://ip/5'
CELERY_RESULT_BACKEND = 'redis://ip:6379/5'

CELERYBEAT_SCHEDULE = {
        'import_data': {
            'task': 'import_data',
            'schedule': timedelta(seconds=10)
        }}
