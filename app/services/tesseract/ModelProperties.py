import os
import shutil

class ModelProperties(object):

    model_path = os.getenv('MODEL_PATH')
    tesseract_env = os.getenv("TESSDATA_PREFIX")
    training_data = os.getenv("TRAINING_DATA")
    stats = os.getenv("STATS_PATH")
    iterations = 500
    pages = 5  # amount of training data (pages)

    def __init__(self, lang, iterations=500, pages=5):
        self.lang = lang
        self.iterations = iterations
        self.pages = pages

    def init_setup(self):
        # empty folder and create new
        dirs = [self.model_path, self.training_data, self.stats]
        for dirr in dirs:
            if os.path.exists(dirr):
                shutil.rmtree(dirr)
            os.mkdir(dirr)
