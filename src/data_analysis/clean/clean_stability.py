import os  # For interacting with the operating system
import numpy as np  # For numerical operations (though not used in the current code)
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For plotting (though not used in the current code)
from scipy.optimize import curve_fit  # For fitting curves to data (though not used in the current code)

def process_stability(FSR_dir, file_name, ref_force):
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
    save_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability_error', file_name)

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
file_name = 'FSR_S4_7.25lbf.csv'
process_stability(FSR_dir, file_name, 7.25)

# Process multiple files at once (uncomment to use)
# file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'processed')
# files = os.listdir(file_path)
# sorted_files_list = sorted(files)

# for file in sorted_files_list[1:]:
#     process_stability(FSR_dir, file, 5)
