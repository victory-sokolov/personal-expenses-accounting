import os


class ModelProperties(object):

    model_path = os.getenv('MODEL_PATH')
    tesseract_env = os.getenv("TESSDATA_PREFIX")
    training_data = os.getenv("TRAINING_DATA")
    iterations = 500
    pages = 5  # amount of training data (pages)

    def __init__(self, lang):
        self.lang = lang
