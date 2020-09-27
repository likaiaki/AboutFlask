from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
session = Session()
csrf = CSRFProtect()


def init_ext(app):
    db.init_app(app)  # 初始化应用
    migrate.init_app(app, db) # 加载数据库迁移命令
    session.init_app(app)  # flask默认的session 存储到 cookie中， flask_session 中的session可是配置让session储存到redis中
    csrf.init_app(app)  # 开启ｃsrf验证csrf只会对修改的请求做验证
