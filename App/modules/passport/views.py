from io import BytesIO

from flask import request, abort, current_app, make_response

from utils.redis_til import save_image_code
from . import passport_blu
from App.utils.captcha import Captcha



@passport_blu.route("/image_code")
def send_image_code():
    """

    :return:
    """
    # 获取参数
    # args: 取到url中？后面的参数
    image_code_id = request.args.get("imageCodeId", None)
    # 2.判断参数是否有值
    if not image_code_id:
        return abort(403)
    # 获取验证码
    text, image = Captcha.gene_graph_captcha()
    # 保存验证吗redis
    try:
        save_image_code(image_code_id, text, 300)
    except Exception as e:
        current_app.logger.error(e)
        abort(500)
    # 将字节流包装到Response对象中,返回前端
    out = BytesIO()
    # 把图片保存到字节流中，并指定格式为png
    image.save(out, 'jpg')
    # 指定文件流指针,从文件最开始开始读
    out.seek(0)
    # 将字节流包装到Response对象中,返回前端
    response = make_response(out.read())
    response.content_type = "image/jpg"
    return response

