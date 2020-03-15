import logging

from colorlog import ColoredFormatter


class Logger():

    log = logging.getLogger('pythonConfig')

    @staticmethod
    def info(message, logger_type):
        log_level = logging.DEBUG
        log_format = "%(log_color)s%(levelname)s: %(log_color)s%(message)s%(reset)s"

        logging.root.setLevel(log_level)
        formatter = ColoredFormatter(log_format)
        stream = logging.StreamHandler()
        stream.setLevel(log_level)
        stream.setFormatter(formatter)

        if not Logger.log.handlers:
            Logger.log.addHandler(stream)
        Logger.log.setLevel(log_level)
        logger_type(message)
