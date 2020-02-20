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


def convert_to_iso_639_1(lang: str):
    """Converts iso_639-2 to iso_639-1."""
    iso = read_json('iso_639-2')[lang]['639-1']
    return iso


def is_lang_supported(font: str, lang: str) -> bool:
    """
    Check if fonts supports specific language
    Parameters:
    arg1(string) font name without extension
    arg2(string) language code in ISO 639-2 standart
    """
    # by default eng is supported mostly for all fonts
    if lang == 'eng' or lang == 'en':
        return True

    full_path = os.path.join(font_path(), f'{font}.ttf')

    process = Popen([
        'fc-query', full_path
    ], stdout=PIPE, stderr=PIPE)

    langs = check_output([
        'grep', '-w', 'lang'
    ], stdin=process.stdout, text=True)
    process.wait()
    lang_list = langs.split('|')

    lang = convert_to_iso_639_1(lang)
    return lang in lang_list
