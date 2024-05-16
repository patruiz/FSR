import os 
import csv
import pandas as pd 

def process_data(FSR, file_name):
    FSR_dir = FSR
    file_name = file_name
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'raw', file_name)
    save_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'processed', file_name)
    
    df = pd.read_csv(file_path, index_col = False)

    drop_rows = []
    for index, row in df.iterrows():
        if row.iloc[2] == ' None':
            drop_rows.append(index)
    df = df.drop(drop_rows)

    loadcell_data, dmm_data = [], []
    for index, row in df.iterrows():
        if row.iloc[0] == 'LoadCell':
            loadcell_data.append([row.iloc[1], row.iloc[2]])
        elif row.iloc[0] == 'DMM':
            dmm_data.append([row.iloc[1], row.iloc[2]])
    
    dmm_dict = dict(dmm_data)
    loadcell_dict = dict(loadcell_data)

    for i in list(dmm_dict.keys()):
        if not i in list(loadcell_dict.keys()):
            dmm_dict.pop(i)

    new_dict = loadcell_dict.copy()

    for i in list(new_dict.keys()):
        if i in list(dmm_dict.keys()):
            value = [float(new_dict[i]), float(dmm_dict[i])]
            new_dict[i] = value
    
    new_df = pd.DataFrame(list(new_dict.values()), columns = ['Load (lbf)', 'Resistance (Ohms)'])
    new_df.to_csv(save_path, index = False)

try:
    os.system('clear')
except Exception:
    os.system('cls')
    pass

FSR_dir = 'FSR_S4'

# Process one file at a time
file_name = 'FSR_S4_8.50lbf2nd' + '.csv'
process_data(FSR_dir, file_name)

# for i in range(1, 11):
#     file_name = f"FSR_S3_CalibrationTest_{i}.csv"
#     process_data(FSR_dir, file_name)

# # Process multiple files at once
# file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'raw')
# files = os.listdir(file_path)
# sorted_files_list = sorted(files)

# for file in sorted_files_list:
#     # print(file)
#     process_data(FSR_dir, file)