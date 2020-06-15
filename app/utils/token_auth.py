

from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,BadSignature, SignatureExpired
from flask import current_app,g
from collections import namedtuple
from app.utils.error_code import AuthFailed,Forbidden
from flask import request
from app.utils.scope import is_in_scope

# HTTPBasicAuth 必须将用户、密码 放在请求头中,
# 传递规范：k:v 格式
#     key=Authorization
#     value=basic base64(syk:123456)


auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])

@auth.verify_password
def verify_password(token, password):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True

def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid')
    except SignatureExpired:
        raise AuthFailed(msg='token is expired')
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']
    allow_scope = is_in_scope(scope, request.endpoint)
    if not allow_scope:
        raise Forbidden()
    return User(uid, ac_type, scope)