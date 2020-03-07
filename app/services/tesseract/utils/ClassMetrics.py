from typing import List

class ClassMetrics(object):

    @staticmethod
    def get_list_of_methods(class_name) -> List:
        return [
            func for func in dir(class_name)
            if callable(
                getattr(class_name, func)
            ) and not func.startswith("_")
        ]

    @staticmethod
    def get_class_name_from_instance(class_name):
        return type(class_name).__name__

