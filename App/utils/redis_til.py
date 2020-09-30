from redis import StrictRedis
from App.settings import envs


# redis_store = None  # type: StrictRedis
config_name = envs.get("development")
redis_store = StrictRedis(host=config_name.REDIS_HOST, port=config_name.REDIS_PORT, decode_responses=True, db=3)


def save_image_code(key, value, timeout=300):
    """
    把验证码存到Redis
    :param key:
    :param value:
    :param timeout:
    :return:
    """
    return redis_store.set(key, value, timeout)

def get_image_code(key):
    """
    从redis中取验证吗
    :param key:
    :return:
    """
    return redis_store.get(key)


def delete_captcha(key):
    return redis_store.delete(key)