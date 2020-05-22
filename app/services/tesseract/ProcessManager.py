import subprocess
from subprocess import PIPE, STDOUT, Popen
from typing import List


class ProcessManager(object):

    @staticmethod
    def create_process(params: List):
        process = subprocess.Popen(
            params, stdout=PIPE, stderr=STDOUT, text=True
        )
        return process

    @staticmethod
    def process_output(process):
        statistics = None
        while process.poll() is None:
            line = process.stdout.readline()
            print(line)
            if line.startswith('At iteration'):
                statistics = line
        process.stdout.close()
        process.kill()
        process.wait()

        return statistics
