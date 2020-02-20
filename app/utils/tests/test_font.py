import unittest

from app.utils.font import is_lang_supported


class TestFont(unittest.TestCase):

    def test_is_lang_supported(self):
        # self.assertTrue(is_lang_supported('OCR-A', 'eng'))
        self.assertFalse(is_lang_supported('OCR-A', 'lav'))


if __name__ == "__main__":
    unittest.main(warnings='ignore')
