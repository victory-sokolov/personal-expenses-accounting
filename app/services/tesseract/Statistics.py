import matplotlib.pyplot as plt
import numpy as np

from app.utils.helpers import read_file


class Statistics(object):

    def plot_data(self, fonts):
        np.random.seed(19680801)
        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        y_pos = np.arange(len(fonts))
        performance = 3 + 10 * np.random.rand(len(fonts))
        error = np.random.rand(len(fonts))

        ax.barh(y_pos, performance, xerr=error, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(fonts)
        ax.invert_yaxis()
        ax.set_xlabel('Performance')
        ax.set_title('Font statistics')

        plt.show()


stat = Statistics()

data = read_file('./stats/before_lav_model_statistics.csv')
stat.plot_data(tuple(data))

# 1.skip header when reading file
