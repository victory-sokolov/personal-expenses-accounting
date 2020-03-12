import os
import shutil


class ModelProperties:

    model_path = os.getenv('MODEL_PATH')
    lstm = f'{model_path}/{os.getenv("LSTM")}'
    tesseract_env = os.getenv("TESSDATA_PREFIX")
    training_data = os.getenv("TRAINING_DATA")
    stats = os.getenv("STATS_PATH")
    trained_data = model_path
    font = None

    def __init__(self, lang, iterations=3000, pages=300):
        self.lang = lang
        self.iterations = iterations
        self.pages = pages

    def init_setup(self):
        dirs = [self.model_path, self.training_data, self.stats]
        for dirr in dirs:
            if not os.path.exists(dirr):
                os.mkdir(dirr)
