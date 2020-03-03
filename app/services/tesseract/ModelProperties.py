import os
import shutil


class ModelProperties(object):

    model_path = os.getenv('MODEL_PATH')
    tesseract_env = os.getenv("TESSDATA_PREFIX")
    training_data = os.getenv("TRAINING_DATA")
    stats = os.getenv("STATS_PATH")

    def __init__(self, lang, iterations=4500, pages=250):
        self.lang = lang
        self.iterations = iterations
        self.pages = pages

    def init_setup(self):
        # empty folder and create new
        dirs = [self.model_path, self.training_data, self.stats]
        for dirr in dirs:
            if not os.path.exists(dirr):
                # shutil.rmtree(dirr)
                os.mkdir(dirr)
