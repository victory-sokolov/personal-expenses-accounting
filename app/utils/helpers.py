"""
Helper Functions
"""
import csv
import os

from font import font_name


def data_to_file(data, filename, path):
    """ Save passed data to text file"""
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


data_to_file(font_name, 'fonts.txt', 'app/tesseract')
