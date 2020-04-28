from flask import Flask

from App.ext import init_ext
from App.modules.user import user
from App.settings import envs


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))

    init_ext(app)

    app.register_blueprint(user, url_prefix="/user")

    return app