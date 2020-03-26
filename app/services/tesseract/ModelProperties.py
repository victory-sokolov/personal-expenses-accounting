import os
import settings

class ModelProperties:

    model_path = os.getenv('MODEL_PATH')
    lstm = f'{model_path}/{os.getenv("LSTM")}'
    tesseract_env = os.getenv("TESSDATA_PREFIX")
    training_data = os.getenv("TRAINING_DATA")
    stats = os.getenv("STATS_PATH")
    trained_data = model_path
    fonts = []

    def __init__(self, lang, iterations=50000, pages=1000):
        self.lang = lang
        self.iterations = iterations
        self.pages = pages

    def init_setup(self):
        dirs = [self.model_path, self.training_data,
                self.stats, f'{ModelProperties.model_path}/traineddata']
        for dirr in dirs:
            if not os.path.exists(dirr):
                os.mkdir(dirr)
