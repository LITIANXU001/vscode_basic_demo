import matplotlib.pyplot as plt

from utils import read_snr_data


snr_values = read_snr_data("data/snr.txt")

experiment_index = range(1, len(snr_values) + 1)

plt.plot(experiment_index, snr_values, marker="o")

plt.xlabel("Experiment Index")
plt.ylabel("SNR (dB)")
plt.title("SNR Measurement Results")

plt.grid(True)

plt.savefig("figures/snr_results.png")

plt.show()