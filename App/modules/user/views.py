from flask import session
from App.modules.user import user
import logging


@user.route("/")
def hello():
    session["name"] = "哈哈哈"
    return "hello"

