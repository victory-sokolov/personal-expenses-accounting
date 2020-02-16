import os
import re
from pathlib import Path, PurePosixPath
from subprocess import PIPE, Popen, check_output


def font_path() -> str:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    path = PurePosixPath(ROOT_DIR).parent.parent
    return f'{path}/fonts'


def get_fonts_names() -> list:
    dir = f'{font_path()}'
    return os.listdir(dir)


def font_name(fonts: list) -> list:
    font_lst = []

    for name in fonts:
        process = Popen(
            ['fc-scan', f'{font_path()}/{name}'], stdout=PIPE, stderr=PIPE)
        full_name = check_output(('grep', 'fullname'), stdin=process.stdout)
        process.wait()
        font_name = re.findall(r'\"(.+?)\"', str(full_name).split(":")[1])[0]
        font_lst.append(font_name)
    return font_lst
