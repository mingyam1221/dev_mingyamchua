daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73],
    ]

from pathlib import Path
import csv

file_path = Path.home() / "temperatures.csv"
file = file_path.open(mode="w", encoding="utf-8", newline = "")
writer = csv.writer(file)

for temp_list in daily_temperatures:
    writer.writerow(temp_list)

file.close()
