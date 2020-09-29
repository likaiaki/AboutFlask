from datetime import datetime

from App.ext import db


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


class User(BaseModel, db.Model):
    """用户"""
    __tablename__ = "info_user"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    nick_name = db.Column(db.String(32), unique=True, nullable=False)  # 用户昵称
    password_hash = db.Column(db.String(128), nullable=False) # 加密密码
    mobile = db.Column(db.String(11), unique=True, nullable=False) # 手机号
    avatar_url = db.Column(db.String(256))  #用户头像路径
    last_login = db.Column(db.DateTime, default=datetime.now())
    is_admin = db.Column(db.Boolean, default=False)
    signature = db.Column(db.String(512))  # 用户签名
    gender = db.Column(
        db.Enum(
            "MAN"
            "WOMAN"
        ),
        default="MAN"
    )


class Blog(BaseModel, db.Model):
    """博客"""
    __tablename__ = "info_blog"
    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    title = db.Column(db.String(256), nullable=False)  # 标题
    source = db.Column(db.String(64), nullable=False)  # 来源
    digest = db.Column(db.String(512), nullable=False)  # 摘要
    index_image_url = db.Column(db.String(256))  # 博客列表图片路径
    category_id = db.Column(db.Integer, db.ForeignKey("info_category.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("info_user.id"))  # 当前blog的作者id
    status = db.Column(db.Integer, default=0)  # 当前blog状态 如果为0代表审核通过，1代表审核中，-1代表审核不通过
    reason = db.Column(db.String(256))  # 未通过原因，status = -1 的时候使用
    # 当前新闻的所有评论
    comments = db.relationship("Comment", lazy="dynamic")


class Comment(BaseModel, db.Model):
    """评论"""
    __tablename__ = "info_comment"

    id = db.Column(db.Integer, primary_key=True)  # 评论编号
    user_id = db.Column(db.Integer, db.ForeignKey("info_user.id"), nullable=False)  # 用户id
    news_id = db.Column(db.Integer, db.ForeignKey("info_blog.id"), nullable=False)  # blog的id
    content = db.Column(db.Text, nullable=False)  # 评论内容
    parent_id = db.Column(db.Integer, db.ForeignKey("info_comment.id"))  # 父评论id
    parent = db.relationship("Comment", remote_side=[id])  # 自关联
    like_count = db.Column(db.Integer, default=0)  # 点赞条数


class CommentLike(BaseModel, db.Model):
    """评论点赞"""
    __tablename__ = "info_comment_like"
    comment_id = db.Column("comment_id", db.Integer, db.ForeignKey("info_comment.id"), primary_key=True)  # 评论编号
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("info_user.id"), primary_key=True)  # 用户编号


class Category(BaseModel, db.Model):

    __tablename__ = "info_category"

    id = db.Column(db.Integer, primary_key=True)  # 分类编号
    name = db.Column(db.String(64), nullable=False)  # 分类名
    news_list = db.relationship('News', backref='category', lazy='dynamic')