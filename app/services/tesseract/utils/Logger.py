import logging

class Logger():

  @staticmethod
  def info(message):
    logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO)
    logging.info(message)

