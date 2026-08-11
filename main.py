from utils import read_snr_data, calculate_statistics


snr_values = read_snr_data("data/snr.txt")

average_snr, max_snr, min_snr = calculate_statistics(snr_values)

print("SNR values:", snr_values)
print("Average SNR:", average_snr)
print("Maximum SNR:", max_snr)
print("Minimum SNR:", min_snr)
