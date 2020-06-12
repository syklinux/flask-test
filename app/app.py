
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from app.utils.error_code import ServerError
from datetime import date


# 蓝图（分离试图函数，并不是太好）

# 自定义jsonfy可以序列化模型开始
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()

class Flask(_Flask):
    json_encoder = JSONEncoder

# 自定义jsonfy可以序列化模型结束