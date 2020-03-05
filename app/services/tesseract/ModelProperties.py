import os
import shutil


class ModelProperties(object):

    model_path = os.getenv('MODEL_PATH')
    default_model_path = f'{model_path}/{os.getenv("DEFAULT_MODEL_PATH")}'
    tesseract_env = os.getenv("TESSDATA_PREFIX")
    training_data = os.getenv("TRAINING_DATA")
    stats = os.getenv("STATS_PATH")

    def __init__(self, lang, iterations=4500, pages=300):
        self.lang = lang
        self.iterations = iterations
        self.pages = pages

    def init_setup(self):
        dirs = [self.model_path, self.training_data, self.stats,
                self.default_model_path]
        for dirr in dirs:
            if not os.path.exists(dirr):
                os.mkdir(dirr)
