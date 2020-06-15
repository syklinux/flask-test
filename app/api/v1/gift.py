from flask import g

from app.utils.error_code import Success, DuplicateGift
from app.utils.redprint import Redprint
from app.utils.token_auth import auth
from app.models.base import db
from app.models.models import Book
from app.models.models import Gift

api = Redprint('gift')


@api.route('/<isbn>', methods=['POST'])
@auth.login_required
def create(isbn):
    uid = g.user.uid
    with db.auto_commit():
        Book.query.filter_by(isbn=isbn).first_or_404()
        gift = Gift.query.filter_by(isbn=isbn, uid=uid).first()
        if gift:
            raise DuplicateGift()
        gift = Gift()
        gift.isbn = isbn
        gift.uid = uid
        db.session.add(gift)
    return Success()