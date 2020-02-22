import os


class ModelProperties(object):

    model_path = os.getenv('MODEl_PATH')
    tesseract_env = os.getenv("TESSDATA_PREFIX")
    training_data = os.getenv("TRAINING_DATA")

    def __init__(self, lang):
        self.lang = lang
        # self.model_name = model_name
