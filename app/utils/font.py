from subprocess import Popen, PIPE, check_output
from pathlib import Path, PurePosixPath
import os
import re


def path() -> str:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    path = PurePosixPath(ROOT_DIR).parent.parent
    return path


def get_fonts_names() -> list:
    dir = f'{path()}/fonts/'
    return os.listdir(dir)
  

def font_name(fonts: list) -> list:
    font_lst = [] 
    font_names = fonts()

    for name in font_names:
        process = Popen(['fc-scan', f'{path()}/fonts/{name}'], stdout=PIPE, stderr=PIPE)
        full_name = check_output(('grep', 'fullname'), stdin=process.stdout)
        process.wait()
        font_name = re.findall(r'\"(.+?)\"', str(full_name).split(":")[1])[0]
        font_lst.append(font_name)
    return font_lst    


print(font_name(get_fonts_names))