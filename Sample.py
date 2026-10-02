import csv
import random

# =========================
# Settings
# =========================

input_file = "flights.csv"
output_file = "flights_sample_1000.csv"
sample_size = 1000

# =========================
# Reservoir Sampling
# =========================

sample = []

with open(input_file, "r", encoding="utf-8-sig", newline="") as file:

    reader = csv.reader(file)

    # Read header
    header = next(reader)

    # Read rows
    for i, row in enumerate(reader):

        # First 1000 rows
        if i < sample_size:
            sample.append(row)

        # After 1000 rows:
        # Randomly replace existing rows
        else:
            j = random.randint(0, i)

            if j < sample_size:
                sample[j] = row

# =========================
# Save Sample
# =========================

with open(output_file, "w", encoding="utf-8-sig", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(header)
    writer.writerows(sample)

print("Done!")
print(f"Sample created: {output_file}")
print(f"Rows: {len(sample)}")