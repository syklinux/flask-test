
from werkzeug.exceptions import HTTPException
from flask import request,json


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we make a mistake!'
    error_code = 999
    data = {}

    def __init__(self, msg=None, code=None, data=None, headers=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        try:
            if data:
                self.data = data.json
        except:
            self.data = {}
        super(APIException,self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            status = self.code,
            msg = self.msg,
            data = self.data
            # request = request.method + ' ' + self.get_url_no_param(),
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [("Content-Type", "application/json; charset=utf-8")]

    def get_url_no_param(self):
        full_path = str(request.full_path)
        main_path = full_path.split('?')[0]
        return main_path
