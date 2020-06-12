
from flask import jsonify, g

from app.utils.error_code import DeleteSuccess, AuthFailed
from app.utils.redprint import Redprint
from app.utils.token_auth import auth
from app.models.base import db
from app.models.models import User
from app.utils.error_code import DataSuccess


api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    # user = User.query.filter_by(id=uid).first_or_404()
    user = User.query.get_or_404(uid)

    return DataSuccess(data=jsonify(user))


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.id
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


# 管理员
@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    pass


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()

@api.route('', methods=['PUT'])
def update_user():
    return 'update qiyue'