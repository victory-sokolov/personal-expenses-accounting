import csv
from collections import defaultdict
from typing import Dict

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

from utils.helpers import read_file


class Statistics(object):

    def plot_data(self, data: Dict, label: str, text: str):
        """Plots data from csv file
            arg1 - data to be plotted accepts dictionary
            arg2 - title text
            arg3 - text (char or word)
        """
        if text != "char" and text != "word":
            print("Type parameter must be either 'char' or 'word'")
            return

        t = 0 if type == 'char' else 1
        fonts = list(data[t].keys())

        dict_values_before = list(data[t].values())
        before = [i[0] for i in dict_values_before]

        dict_values_after = list(data[t].values())
        after = [i[1] for i in dict_values_after]

        index = np.arange(len(fonts))
        bar_width = 0.30
        fig, ax = plt.subplots()
        charErrorBar = ax.bar(index - bar_width/2,
                              before, bar_width, label='Before')
        wordErrorBar = ax.bar(index + bar_width/2,
                              after, bar_width, label='After')

        ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        ax.set_title(label + ' statistics')
        ax.set_ylabel(label + " rate")
        ax.set_xticks(index)
        ax.set_xticklabels(fonts)

        ax.legend()
        plt.show()

    def get_stats(self):
        font_before = defaultdict(list)
        font_after = defaultdict(list)

        with open('./stats/before_lav_model_statistics.csv') as f:
            reader = csv.reader(f)
            next(reader, None)
            for line in reader:
                font_before[line[0]].append(float(line[1]))
                font_after[line[0]].append(float(line[2]))

        with open('./stats/after_lav_model_statistics.csv') as f:
            reader = csv.reader(f)
            next(reader, None)
            for line in reader:
                font_before[line[0]].append(float(line[1]))
                font_after[line[0]].append(float(line[2]))

        return [font_before, font_after]


stat = Statistics()
data = stat.get_stats()
stat.plot_data(data, "Character error", "char")
