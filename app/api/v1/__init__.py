

## 红图 入口
from flask import Blueprint

from app.api.v1 import client,token,user,book

def create_blueprint_v1():
    bp_v1 = Blueprint('v1',__name__)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    return bp_v1