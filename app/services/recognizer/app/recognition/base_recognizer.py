from abc import ABC, abstractmethod

class Recognizer(ABC):

    @abstractmethod
    def recognize(self, image_path: str):
        raise 
