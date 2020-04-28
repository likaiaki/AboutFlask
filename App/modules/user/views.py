from App.modules.user import user


@user.route("/")
def hello():
    return "hello"