import os  # For interacting with the operating system
import math
import numpy as np  # For numerical operations (though not used in the current code)
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For plotting (though not used in the current code)
from scipy.optimize import curve_fit  # For fitting curves to data (though not used in the current code)

def round_to_sigfigs(num, sigfigs):
    if num == 0:
        return 0
    else:
        try: 
            return round(num, sigfigs - int(math.floor(math.log10(abs(num)))) - 1)
        except:
            pass

def clean_stability(FSR_dir, file_name, ref_force):
    """
    Process stability data from a CSV file, filter it based on a reference force,
    and save the processed data to a new CSV file.

    Parameters:
    FSR_dir (str): Directory containing the FSR data.
    file_name (str): Name of the file to process.
    ref_force (float): Reference force to filter the data.
    """
    # Construct the file paths for reading the input file and saving the output file
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'processed', file_name)
    save_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file_name)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path, index_col=None)

    # Initialize variables for processing
    data = {}  # Dictionary to store segments of data exceeding the reference force
    flag, new_data, counter = False, [], 0  # Flags and counters for processing
    index_dict, index_data = {}, []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        if row.iloc[0] > ref_force:  # Check if the force value exceeds the reference force
            flag = True
            new_data.append([float(row.iloc[0]), float(row.iloc[1])])
            index_data.append(index)
        else:
            if flag:
                data[counter] = new_data  # Store the segment in the dictionary
                index_dict[counter] = index_data
                counter += 1  # Increment the counter
                flag = False  # Reset the flag
                new_data, index_data = [], []  # Clear the new_data list

    # print(index_dict)

    # Process the collected data to find the previous value before the closest match to the reference force
    new_data = {}
    for i in list(data.keys()):
        if len(data[i]) == 1:
            new_data[i] = data[i]  # If only one data point, keep it
        else:
            curr, diff, prev_val = 0, 100, None
            for j in range(len(data[i])):
                diff = abs(ref_force - data[i][j][0])
                if diff < curr or curr == 0:
                    curr = diff
                    if j > 0:
                        prev_val = data[i][j-1]
                    else:
                        prev_val = data[i][j]
            new_data[i] = prev_val  # Store the previous data point

    # Convert the processed data into a DataFrame and save it as a CSV file
    data_df = pd.DataFrame.from_dict(new_data, orient='index', columns=['Force (lbf)', 'Resistance (Ohms)'])
    data_df["Force (lbf)"] = round(data_df["Force (lbf)"], 3)
    # data_df["Resistance (Ohms)"] = round(data_df["Resistance (Ohms)"]) #Non rounded Analysis
    data_df["Resistance (Ohms)"] = data_df["Resistance (Ohms)"].apply(lambda x: round_to_sigfigs(x, 3)) # Rounded analysis 
    data_df.to_csv(save_path, index=False)

# Clear the console screen
try:
    os.system('clear')
except Exception:
    os.system('cls')
    pass

# Directory and file names
FSR_dir = 'FSR_S4'

# Process one file at a time
# file_name = 'FSR_S4_5.00lbf2nd.csv'
# clean_stability(FSR_dir, file_name, 5.00)

# Process multiple files at once (uncomment to use)
# file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'processed')
# files = os.listdir(file_path)
# sorted_files_list = sorted(files)

# for file in sorted_files_list[1:]:
#     process_stability(FSR_dir, file, 5)

#process FSR_S4 data
names = ["4.00", "4.25", "4.50", "4.75", "5.00", "5.25", "5.50", "5.75", "6.00", "6.25", "6.50", "6.75", "7.00", "7.25", "7.50", "7.75", "8.00", "8.25", "8.50", "8.75", "9.00"]

for i in names:
    FSR_dir = "FSR_S4"
    part_file_name = f"FSR_S4_{i}lbf"
    file_name = part_file_name + ".csv"
    clean_stability(FSR_dir, file_name, float(i))
    