import os
from subprocess import PIPE, Popen, check_output

from font import font_path

LANG = "lav"
TRAIN_FOLDER = "train_data"
MODEL = "model_output"
TESSERACT_ENV = os.getenv("TESSDATA_PREFIX")


def generate_training_data():
    max_pages = 20
    path = font_path()
    fonts = get_fonts_names()

    process = Popen([
        'tesstrain.sh',
        f'--fonts_dir {path}',
        f'--fontlist {fonts}',
        f'--lang {LANG}',
        '--noextract_font_properties',
        '--linedata_only',
        f'--langdata_dir {TESSERACT_ENV}/langdata_lstm',
        f'--tessdata_dir {TESSERACT_ENV}',
        '--save_box_tiff',
        f'--maxpages {max_pages}',
        f'--output_dir {TRAIN_FOLDER}'
    ], stdout=PIPE, stderr=PIPE)

    process.wait()
    stdout, stderr = process.communicate()


def evaluate():
    font_checkpoint = "hypermarket_checkpoint"

    process = Popen([
        'lstmeval',
        '--model', f'../tesseract/{MODEL}/{font_checkpoint}',
        '--traineddata', f'../tesseract/{MODEL}/{LANG}.traineddata',
        '--eval_listfile', f'../tesseract/{TRAIN_FOLDER}/{LANG}.training_files.txt'
    ], stdout=PIPE, stderr=PIPE)
    process.wait()
    stdout, stderr = process.communicate()

    print(stdout)
    print(stderr)


def combine():
    checkpoint = ""

    process = Popen([
        'lstmtraining',
        '--stop_training',
        f'- -continue_from model_output', checkpoint,
        f'--traineddata', '{TESSDATA_ENV}/{LANG}.traineddata',
        f'--model_output', '{MODEL}/{LANG}.traineddata'
    ], stdout=PIPE, stderr=PIPE)
    process.wait()
    stdout, stderr = process.communicate()
    # --continue_from model_output /$checkpoint \
    # --traineddata $TESSDATA_PREFIX /$lang.traineddata \
    # --model_output model_output/latvian.traineddata


def extract_recognition_model():
    pass


def fine_tune():
    pass


evaluate()
