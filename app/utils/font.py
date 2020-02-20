import os
import re
import subprocess
from pathlib import Path, PurePosixPath
from subprocess import PIPE, Popen, check_output

from app.utils.helpers import read_json


def font_path() -> str:
    """Return font full path"""
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    path = PurePosixPath(ROOT_DIR).parent.parent
    return f'{path}/fonts'


def get_fonts_names() -> list:
    """
    Get font names in directory
    with extension: .ttf
    """
    dir = f'{font_path()}'
    dir_content = os.listdir(dir)
    font_list = [font for font in dir_content if font.endswith('.ttf', -4)]
    return font_list


def font_name() -> list:
    """Get fonts names from fc-scan command"""
    font_lst = []
    fonts = get_fonts_names()

    for name in fonts:
        process = Popen(
            ['fc-scan', f'{font_path()}/{name}'], stdout=PIPE, stderr=PIPE)
        full_name = check_output(('grep', 'fullname'), stdin=process.stdout)
        process.wait()
        font_name = re.findall(r'\"(.+?)\"', str(full_name).split(":")[1])[0]
        font_lst.append(font_name)
    return font_lst


def is_lang_supported(font: str, lang: str):
    """
    Check if fonts supports specific language
    Parameters:
    arg1(string) font name without extension
    arg2(string) language code in ISO 639-1 standart
    """

    # by default eng is suppiorted mostly for all fonts
    if lang == 'eng' or lang == 'en':
        return True

    # convert 639-2 to 639-1
    l = read_json('../tesseract/iso_639-2')[lang]['639-1']
    font = f'{font}.ttf'
    path = font_path()
    full_path = os.path.join(path, font)

    process = Popen([
        'fc-query', full_path
    ], stdout=PIPE, stderr=PIPE)

    langs = check_output([
        'grep', '-w', 'lang'
    ], stdin=process.stdout, text=True)
    process.wait()
    lang_list = langs.split('|')

    return l in lang_list


#print(is_lang_supported('Hypermarket W00 Light', 'lav'))
