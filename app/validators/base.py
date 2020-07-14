
from wtforms import Form

from app.utils.error_code import ParameterError
from flask import request


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        vaild = super(BaseForm,self).validate()
        if not vaild:
            raise ParameterError(msg=self.errors)
        return self


