

## 红图 入口
from flask import Blueprint

from app.api.v1 import tasks


def create_blueprint_v1():
    bp_v1 = Blueprint('v1',__name__)
    tasks.api.register(bp_v1)
    return bp_v1