from typing import List

from app.services.tesseract.TrainingDataGenerator import TrainingDataGenerator


class ClassMetrics(object):

    @staticmethod
    def get_list_of_methods(class_name) -> List:
        return [
            func for func in dir(class_name)
            if callable(
                getattr(class_name, func)
            ) and not func.startswith("__")
        ]
