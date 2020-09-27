import logging
import os
from redis import StrictRedis


class Config(object):
    SECRET_KEY = "/OC1aG5EBPwK+SlVQfEq9BPkSjinoqnWciF6UrZCr+1APfC/7lNHTj4dqHqQLn5a"
    LOG_LEVEL = logging.ERROR


class DevelopmentConfig(Config):
    DEBUG = True
    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:dashani521@127.0.0.1:3306/flaskdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 在请求结束时候，如果指定此配置为 True ，那么 SQLAlchemy 会自动执行一次 db.session.commit()操作
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # Redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # Session保存配置
    SESSION_TYPE = "redis"
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 指定 Session 保存的 redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400
    # 开发环境设置日志等级为errio
    LOG_LEVEL = logging.ERROR


class TestingConfig(Config):
    """单元测试环境下的配置"""
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """生产环境下的配置"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING


envs = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
