import os 
import csv
import pandas as pd

file_name = r'Calibration Data 03May24 FSR-N1.csv'
file_path = os.path.join(os.getcwd(), 'data', 'FSR_TEST', 'calibration', file_name)
print(file_path)

force, ohms = [], []
with open(file_path) as csvfile:
    csv_file = csv.reader(csvfile)
    next(csv_file)
    for row in csv_file:
        if float(row[0]) > 1:
            force.append(row[0]), ohms.append(row[1])


df = pd.DataFrame([force, ohms], columns = ['Load (lbf)', 'Resistance (Ohms)'])
print(df)