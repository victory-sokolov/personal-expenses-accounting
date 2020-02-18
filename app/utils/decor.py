from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s')

def exectime(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = start - datetime.now()
        logging.info(f'Execution time: {end}')
        return result
    return wrapper
