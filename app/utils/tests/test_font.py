import unittest

from app.utils.font import is_lang_supported


class TestFont(unittest.TestCase):

    def test_is_lang_supported(self):
        self.assertTrue(is_lang_supported('OCR-A', 'eng'))
        self.assertTrue(is_lang_supported('Hypermarket W00 Light', 'lav'))
        self.assertFalse(is_lang_supported('OCR-A', 'lav'))


if __name__ == "__main__":
    unittest.main(verbosity=2)
