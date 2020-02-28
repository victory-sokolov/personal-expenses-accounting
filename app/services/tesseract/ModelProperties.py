import os
import shutil

class ModelProperties(object):

    model_path = os.getenv('MODEL_PATH')
    tesseract_env = os.getenv("TESSDATA_PREFIX")
    training_data = os.getenv("TRAINING_DATA")
    iterations = 500
    pages = 5  # amount of training data (pages)

    def __init__(self, lang):
        self.lang = lang

    def init_setup(self):
        # empty folder and create new
        dirs = [self.model_path, self.training_data]
        for dirr in dirs:
            if os.path.exists(dirr):
                shutil.rmtree(dirr)
            os.mkdir(dirr)

        # delete stats csv if exists
        stats_csv = './model_statistics.csv'
        if os.path.isfile(stats_csv):
            os.remove(stats_csv)
