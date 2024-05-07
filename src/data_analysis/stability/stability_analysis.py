import os 
import csv
import numpy as np
import pandas as pd 

def power_func(x, A = 22121.19563, b = -0.9704):
    return A * np.power(x, b)

def percenterror_func(acc, theo):
    return ((acc - theo) / theo) * 100

def stability_analysis(FSR_dir, file_name):
    # data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file_name)
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file_name)
    temp_file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', 'temp_' + file_name)
        
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

                    row.append(round(expected_resistance, 5))
                    row.append(round(percent_error, 2))
                    writer.writerow(row)
                except:
                    pass

    os.remove(file_path)
    os.rename(temp_file_path, file_path)

os.system('clear')
# os.system('cls')
FSR_dir = 'FSR_S3'
file_name = 'FSR_S3_Stability_3' + '.csv'
stability_analysis(FSR_dir, file_name)
