import logging
from datetime import datetime
from functools import wraps


def timing(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        elapsed_time = datetime.now() - start
        logging.info('Elapsed time: %s', elapsed_time)
        return result
    return wrap
