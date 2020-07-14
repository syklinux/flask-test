
from app.api.v1 import create_blueprint_v1
from app.app import Flask

# 蓝图
def register_blueprints(app):
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')

# models
def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all() #必须在 app的上下文中才能生效

def create_app():
    from app.utils.tsk import celery
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    celery.conf.update(app.config)
    register_blueprints(app)
    register_plugin(app)
    return app