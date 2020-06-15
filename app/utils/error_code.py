
from app.utils.error import APIException

class Success(APIException):
    code = 201
    msg = 'ok'

class DataSuccess(APIException):
    code = 200
    msg = "ok"

class ClientTypeError(APIException):
    code = 500
    msg = 'client is invalid'

class ParameterError(APIException):
    code = 400
    msg = 'invalid error'

class ServerError(APIException):
    code = 502
    msg = '服务器出错，请联系ops'

class ResourceError(APIException):
    msg = 'xxx'
    code = 409

class NotFound(APIException):
    msg = 'the resource are not found'
    code = 404

class AuthFailed(APIException):
    msg = 'authorization failed'
    code = 401

class DeleteSuccess(APIException):
    msg = 'authorization failed'
    code = 401

class Forbidden(APIException):
    code = 403
    msg = 'forbidden, not in scope'