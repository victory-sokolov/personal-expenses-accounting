import subprocess

from app.utils.font import is_lang_supported, font_path
from app.utils.helpers import read_file

class GenerateTrainingData():

    def generate_training_data(self, pages=250):
        """Generates training data"""
        path = font_path()
        font_list = read_file('fonts.txt')

        # if language is supported then generate training data
        font = 'OCR-A'
        if is_lang_supported(font, self.lang):
            process = subprocess.call([
                'tesstrain.sh',
                '--fonts_dir', path,
                '--fontlist', 'OCR-A',
                '--lang', self.lang,
                '--noextract_font_properties',
                '--linedata_only',
                '--langdata_dir', f'{self.tesseract_env}/langdata_lstm',
                '--tessdata_dir', self.tesseract_env,
                '--save_box_tiff',
                '--maxpages', str(pages),
                '--output_dir', self.train_folder
            ])
        else:
            print(f"Font {font} doesn't support {self.lang} language")
        return process
