import os


class ModelProperties:

    def __init__(self, lang, model_path, model_name):
        self.lang = lang
        self.model_path = os.getenv('MODEl_PATH')
        self.model_name = model_name
