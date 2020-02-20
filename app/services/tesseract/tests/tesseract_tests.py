import unittest

from app.tesseract.training import Training


class TestingTrainingTesseract(unittest.TestCase):
    """Tests for Tesseract training engine"""
    def __init__(self):
        super()
        self.training = Training()

    def test_generation_of_data(self, pages):
        """Ensure training data is being generated"""
