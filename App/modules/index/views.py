from App.modules.index import index_bul
from flask import render_template, current_app

# 渲染首页数据
@index_bul.route("/")
def index():
    return render_template("news/index.html")


# 返回图标
@index_bul.route("/favicon.ico")
def favicon():
    return current_app.send_static_file("news/favicon.ico")