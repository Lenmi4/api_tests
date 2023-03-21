import logging
from functools import wraps

logger = logging.getLogger("api")


def logging(message):
    def wrapper(function):
        @wraps(function)
        def inner(*args, **kwargs):
            logger.info(message)
            res = function(*args, *kwargs)
            return res

        return inner

    return wrapper()
