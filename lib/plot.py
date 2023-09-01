import numpy as np
import matplotlib.pyplot as plt
import csv

def plot_data(title, xlabel, ylabel, labels, data_points, display=True, save=False, file_name="MA_4064_plot.py"):
    fig, axes = plt.subplots()
    
    processed_data = []
    for set in data_points:
        x, y = np.array(set).T
        processed_data.append((x,y))

    axes.set_title(title)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)

    for x, set in enumerate(processed_data):
        axes.plot(*set, label=labels[x])
    
    axes.legend()

    if save: fig.savefig(file_name, bbox_inches='tight')
    if display: plt.show()

def export_data(file_name, column_names, column_data):
    with open(file_name, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow(column_names)

        for row in range(len(column_data[0])):
            csv_writer.writerow([column[row] for column in column_data ])
