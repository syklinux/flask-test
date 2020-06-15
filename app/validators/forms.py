
from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import DataRequired, length, Email, Regexp
from app.utils.enums import ClientTypeEnum
from app.models.models import User
from app.utils.error import APIException
from app.utils.error_code import ResourceError
from app.validators.base import BaseForm as Form

class ClientForm(Form):
    account = StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client

class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='invalidate email')])
    secret = StringField(validators=[DataRequired(), Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')])
    nickname = StringField(validators=[DataRequired(message='不允许为空'), length(min=2,max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            text = {
                'account': '该邮箱已存在!'
            }
            raise ResourceError(msg=text)

    def validate_nickname(self, value):
        if User.query.filter_by(nickname=value.data).first():
            text = {
                'nickname':'该名称已存在!'
            }
            raise ResourceError(msg=text)

class TokenForm(Form):
    token = StringField(validators=[DataRequired()])


class BookSearchForm(Form):
    q = StringField(validators=[DataRequired()])