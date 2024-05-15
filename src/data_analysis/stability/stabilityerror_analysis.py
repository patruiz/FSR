import os 
import csv
import numpy as np
import pandas as pd 

def power_func(x, A = 25494.51322, b = -1.16791):
    return A * np.power(x, b)

def percenterror_func(acc, theo):
    return ((acc - theo) / theo) * 100

def stabilityerror_analysis(FSR_dir, file_name):
    # data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file_name)
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability_error', file_name)
    temp_file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability_error', 'temp_' + file_name)
        
    with open(file_path, encoding='utf-8', errors='replace') as csvfile:
        with open(temp_file_path, mode='w', newline='', encoding='utf-8') as temp_file:
            
            csv_file = csv.reader((line.replace('\0', '') for line in csvfile))
            writer = csv.writer(temp_file)
            
            header = next(csv_file)
            header.append('Expected Resistance (Ohms)')
            header.append('Percent Error (%)')
            writer.writerow(header)
            
            for row in csv_file:
                try:
                    force = float(row[0])
                    measured_resistance = float(row[1])
                    expected_resistance = power_func(force)
                    percent_error = percenterror_func(measured_resistance, expected_resistance)

                    row.append(round(expected_resistance))
                    row.append(round(percent_error, 2))
                    writer.writerow(row)
                except:
                    pass

    os.remove(file_path)
    os.rename(temp_file_path, file_path)

try:
    os.system('clear')
except Exception:
    os.system('cls')

# Analyze One File at a Time
# FSR_dir = 'FSR_S4'
# file_name = 'FSR_S4_4.00lbf' + '.csv'
# stabilityerror_analysis(FSR_dir, file_name)

# Analysis for FSR S4
names = ["4.00", "4.25", "4.50", "4.75", "5.00", "5.25", "5.50", "5.75", "6.00", "6.25", "6.50", "6.75", "7.00", "7.25", "7.50", "7.75", "8.00", "8.25", "8.50", "8.75", "9.00"]

for i in names:
    FSR_dir = "FSR_S4"
    file_name = f"FSR_S4_{i}lbf"
    full_filename = file_name + ".csv"
    stabilityerror_analysis(FSR_dir, full_filename)
