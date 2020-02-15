import os
import subprocess
import sys
from subprocess import PIPE, Popen, check_output

from app.utils.font import font_path, get_fonts_names

LANG = "lav"
TRAIN_FOLDER = "train_data"
MODEL = "model_output"
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
    font_checkpoint = "hypermarket_checkpoint"
    logfile = open('logfile', 'w')

    process = subprocess.check_output([
        'lstmeval',
        '--model', f'{MODEL}/{font_checkpoint}',
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
    checkpoint = ""

    process = subprocess.check_output([
        'lstmtraining',
        '--stop_training',
        f'- -continue_from model_output', checkpoint,
        f'--traineddata', '{TESSDATA_ENV}/{LANG}.traineddata',
        f'--model_output', '{MODEL}/{LANG}.traineddata'
    ])


def extract_recognition_model():
    process = subprocess.check_output([
        'combine_tessdata -e',
        f'{TESSERACT_ENV}/{LANG}.traineddata'
    ])


def fine_tune():
    pass


# evaluate()

evaluate_default()
