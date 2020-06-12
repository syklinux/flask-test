
# from app.extensions import db,migrate,whooshee
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import Base,db
from sqlalchemy import Column,Integer,String,SmallInteger
from app.utils.error_code import NotFound, AuthFailed

class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True, nullable=False)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    def keys(self):
        return ['id', 'email', 'nickname', 'auth']

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        # scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        # return {'uid': user.id, 'scope': scope}
        return {'uid': user.id }

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

