"""
Helper Functions
"""
import csv
import json
import os


def data_to_file(data, filename, path):
    """Save passed data to text file"""
    file_path = os.path.join(path, filename)

    # if func is passed as argument
    if callable(data):
        dat = data()
    else:
        dat = data

    with open(file_path, 'a', newline='') as f:
        for line in dat:
            writer = csv.writer(f)
            writer.writerow([line])


def read_file(file_name) -> list:
    """Read specified file"""
    with open(file_name) as f:
        reader = csv.reader(f)
        content = [line[0] for line in reader]
    return content


def read_json(file):
    with open(f'{file}.json') as f:
        return json.load(f)
