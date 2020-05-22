import os
import unittest

from base.ProcessManager import ProcessManager
from ModelExtractor import ModelExtractor
from ModelProperties import ModelProperties
from TrainingDataGenerator import TrainingDataGenerator


class TestingTrainingTesseract(unittest.TestCase):
    """Tests for Tesseract training engine"""

    def __init__(self, *args, **kwargs):
        self.props = ModelProperties('lav')
        self.proc = ProcessManager()
        super(TestingTrainingTesseract, self).__init__(*args, **kwargs)

    def test_generation_of_data(self):
        """Ensure training data is being generated"""
        training = TrainingDataGenerator('lav', 5, self.props, self.proc)
        data = training.generate_training_data()
        self.assertEqual(data, 0)

    def test_model_extractor(self):
        """Test Model Extractor"""
        ModelExtractor("lav", self.props,
                       self.proc).extract_recognition_model()
        self.assertTrue(os.path.isfile(f'{self.props.model_path}/lav.lstm'))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingTrainingTesseract)
    unittest.TextTestRunner(verbosity=2).run(suite)
