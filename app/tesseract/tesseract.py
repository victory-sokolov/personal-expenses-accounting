import os
import subprocess
import sys
from subprocess import PIPE, Popen, check_output

from app.utils.font import font_path, get_fonts_names

LANG = "lav"
TRAIN_FOLDER = "train_data"
MODEL = "model_output/"
TESSERACT_ENV = os.getenv("TESSDATA_PREFIX")


def generate_training_data():
    max_pages = 20
    path = font_path()
    fonts = get_fonts_names()

    process = subprocess.call([
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
    ])
    process.wait()
    print(process)


def evaluate():
    font_checkpoint = "hypermarket"
    logfile = open('logfile', 'w')

    process = subprocess.check_output([
        'lstmeval',
        '--model', f'{MODEL}/{font_checkpoint}_checkpoint',
        '--traineddata', f'{MODEL}/{LANG}.traineddata',
        '--eval_listfile', f'{TRAIN_FOLDER}/{LANG}.training_files.txt'
    ])

    print(process)


def evaluate_default():
    process = subprocess.check_output([
        'lstmeval',
        '--model', f'{LANG}.lstm',
        '--traineddata', f'{TESSERACT_ENV}/{LANG}.traineddata',
        '--eval_listfile', f'{TRAIN_FOLDER}/{LANG}.training_files.txt'
    ])
    print(process)


def combine():
    checkpoint = "hypermarket"

    process = subprocess.check_output([
        'lstmtraining',
        '--stop_training',
        '--continue_from', f'model_output/{checkpoint}_checkpoint',
        '--traineddata', f'{TESSERACT_ENV}/{LANG}.traineddata',
        '--model_output', f'{MODEL}/{LANG}.traineddata'
    ])


def extract_recognition_model():
    process = subprocess.check_output([
        'combine_tessdata', '-e',
        f'{TESSERACT_ENV}/{LANG}.traineddata',
        f'{LANG}.lstm'
    ])


def fine_tune():
    process = subprocess.check_output([
        'lstmtraining',
        '--continue_from', f'{LANG}.lstm',
        '--model_output', f'{MODEL}/hypermarket',
        '--traineddata', f'{TESSERACT_ENV}/{LANG}.traineddata',
        '--train_listfile', f'{TRAIN_FOLDER}/{LANG}.training_files.txt',
        '--max_iterations', '400'
    ])
    print(process)


extract_recognition_model()
# fine_tune()
