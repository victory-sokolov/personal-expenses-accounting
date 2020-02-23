import os

class ModelProperties(object):

    model_path = os.getenv('MODEl_PATH')
    tesseract_env = os.getenv("TESSDATA_PREFIX")
    training_data = os.getenv("TRAINING_DATA")
    iterations = 4500
    pages = 5  # amount of training data (pages)

    def __init__(self, lang):
        self.lang = lang
