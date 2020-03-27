import os
from dotenv import load_dotenv
class ModelProperties:
    load_dotenv()
    model_path = os.getenv('MODEL_PATH')
    training_data = os.getenv("TRAINING_DATA")
    stats = os.getenv("STATS_PATH")
    tessdata = os.getenv("TESSDATA_PREFIX")
    fonts = []

    def __init__(self, lang, iterations=200, pages=5):
        self.lang = lang
        self.iterations = iterations
        self.pages = pages

    def init_setup(self):
        dirs = [self.model_path, self.training_data,
                self.stats, f'{ModelProperties.model_path}/traineddata']
        for dirr in dirs:
            if not os.path.exists(dirr):
                os.mkdir(dirr)
