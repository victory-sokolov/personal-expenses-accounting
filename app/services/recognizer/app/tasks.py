from app import celery
from app.services.recogniser.app.recognition import recognizer

class RecognizerTask(celery.Task):
    autoretry_for = (Exception, KeyError)
    retry_kwargs = {'max_retries': 3}
    retry_backoff = True

    def __init__(self, lang: str, image):
        self.lang = lang
        self.image = image

    def run(self, *args, **kwargs):
        recognizer = recognizer(self.lang)
        data = recognizer.recognize_factory(self.image)
        return data
