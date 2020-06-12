
from wtforms import Form

from app.utils.error_code import ParameterError
from flask import request

class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm,self).__init__(data=data)

    def validate_for_api(self):
        vaild = super(BaseForm,self).validate()
        if not vaild:
            raise ParameterError(msg=self.errors)
        return self