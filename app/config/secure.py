
# import os
#
# basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#
# class Config(object):
#     SECRET_KEY = '\xe4\xf5\xd7F\xf6\xb3kMr"\xa5\xff\t\xa1}\xb2\x00\xe0\x01\xf3\xd5\xce@6'
#
# class DevConfig(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Syk_77283720@120.78.171.189:3306/flask_test"
#
# config_map = {
#     'development': DevConfig,
# }


SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Syk_77283720@120.78.171.189:3306/flask_test"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '\xe4\xf5\xd7F\xf6\xb3kMr"\xa5\xff\t\xa1}\xb2\x00\xe0\x01\xf3\xd5\xce@6'
