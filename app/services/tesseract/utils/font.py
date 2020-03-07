import json
import os
import re
from pathlib import Path, PurePosixPath
from subprocess import PIPE, Popen, check_output
from typing import List

from app.services.tesseract.utils.helpers import read_json


def font_path() -> str:
    """Return font full path"""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    path = PurePosixPath(root_dir).parent.parent.parent.parent
    return f'{path}/fonts'


def get_fonts_names_in_dir() -> List:
    """
    Get font names in directory
    with extension: .ttf
    """
    directory = f'{font_path()}'
    print(directory)
    dir_content = os.listdir(directory)
    font_list = [font for font in dir_content if font.endswith('.ttf', -4)]
    return font_list


def get_font_names() -> List:
    """Get original font names."""
    path = font_path()
    fonts_output = check_output([
        'text2image',
        '--fonts_dir', path,
        '--list_available_fonts'
    ], text=True)
    fonts = re.sub('\\d:', '', fonts_output).split("\n")
    return [font.strip() for font in fonts if font]


def fonts_to_json():
    fonts = get_font_names()
    data = None

    json_file = 'fonts.json'
    # if file exists reads it content
    if os.path.isfile(json_file):
        data = read_json('fonts')

    dat = {}
    for font in fonts:
        dat[font] = {'skip': False}

    keys = dat.keys()
    if data:
        for key in keys:
            if key not in data:
                data[key] = {'skip': False}
    else:
        data = dat

    if data:
        with open(json_file, 'w') as file:
            json.dump(data, file)


def fonts_names(font_list: List) -> List:
    """Get fonts names from fc-scan command"""
    font_lst = []

    for name in font_list:
        with Popen(['fc-scan', f'{font_path()}/{name}.ttf'], stdout=PIPE, stderr=PIPE) as proc:
            full_name = check_output(('grep', 'fullname'), stdin=proc.stdout)
            font_name = re.findall(
                r'\"(.+?)\"', str(full_name).split(":")[1])[0]
            font_lst.append(font_name)
    proc.kill()
    return font_lst


def convert_to_iso_639_1(lang: str) -> str:
    """Converts iso_639-2 to iso_639-1."""
    iso = read_json('./utils/iso_639-2')[lang]['639-1']
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
    full_path = os.path.join(font_path(), f'{font}')
    with Popen(['fc-query', full_path], stdout=PIPE, stderr=PIPE) as proc:
        langs = check_output([
            'grep', '-w', 'lang'
        ], stdin=proc.stdout, text=True)
    proc.kill()
    lang_list = langs.split('|')
    lang = convert_to_iso_639_1(lang)
    return lang in lang_list


def supported_fonts(fonts: List, lang: str) -> List:
    """Return list of supported fonts for passed language."""
    fonts_list = []
    for font in fonts:
        if is_lang_supported(font, lang):
            fonts_list.append(font.split(".")[0])
    return fonts_list
