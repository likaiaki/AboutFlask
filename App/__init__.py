import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from App.ext import init_ext
from App.modules.user import user
from App.settings import envs
# import App.settings


def setup_log(config_name):
    """配置日志"""
    # 设置日志的记录等级
    logging.basicConfig(level=envs[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(env):
    config_name = envs.get(env)
    setup_log(env)
    app = Flask(__name__)
    app.config.from_object(config_name)
    init_ext(app)
    app.register_blueprint(user, url_prefix="/user")
    return app


