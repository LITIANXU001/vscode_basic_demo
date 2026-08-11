import numpy as np


def read_snr_data(filepath):
    snr_values = []

    with open(filepath, "r") as file:
        lines = file.readlines()

    for line in lines:
        snr = float(line.strip())
        snr_values.append(snr)

    return snr_values


def calculate_statistics(values):
    values = np.array(values)

    average = np.mean(values)
    maximum = np.max(values)
    minimum = np.min(values)

    return average, maximum, minimum