import os 
import numpy as np
import pandas as pd 

def process_capability(FSR_dir, file_name):
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'processed', file_name)
    save_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'calibration', file_name)

    df = pd.read_csv(file_path, index_col = None)

    delete_rows = []
    for index, row in df.iterrows():
        if not (float(row.iloc[0]) >= 4.00 and float(row.iloc[0]) <=11.00):
            delete_rows.append(index)

    df = df.drop(delete_rows)

    df.to_csv(save_path, index = False)



FSR_dir = 'FSR_S3'
file_name = 'FSR_S3_Calibration_PostStability_3' + '.csv'
process_capability(FSR_dir, file_name)