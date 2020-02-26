import subprocess
from subprocess import PIPE, STDOUT, Popen
from typing import List


class ProcessManager(object):

    @staticmethod
    def create_process(params: List):
        return subprocess.Popen(
            params, stdout=PIPE, stderr=STDOUT, text=True
        )
