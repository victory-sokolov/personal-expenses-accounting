import unittest

from app.utils.font import (
    is_lang_supported,
    convert_to_iso_639_1
)


class TestFont(unittest.TestCase):

    def test_is_lang_supported(self):
        self.assertTrue(is_lang_supported('OCR-A', 'eng'))
        self.assertTrue(is_lang_supported('Hypermarket W00 Light', 'lav'))
        self.assertFalse(is_lang_supported('OCR-A', 'lav'))

    def test_convert_to_iso_639_1(self):
        self.assertEqual(convert_to_iso_639_1('lav'), 'lv')
        self.assertEqual(convert_to_iso_639_1('eng'), 'en')

if __name__ == "__main__":
    unittest.main(verbosity=2)
