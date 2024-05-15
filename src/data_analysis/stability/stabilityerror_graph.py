import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def stabilityerror_graph(FSR_dir, file_name, graph_title = "Graph"):
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability_error', file_name)
    
    df = pd.read_csv(file_path, index_col = False)
    
    error_data = []
    for index, row in df.iterrows():
        error_data.append(np.abs(row.iloc[3]))

    print(f'Average Error: {round(np.average(np.abs(error_data)), 4)}')
    print(f'Maximum Error: {np.max(np.abs(error_data))}')
    print(f'Minimum Error: {np.min(np.abs(error_data))}')
    print(f'Standard Deviation: {round(np.std(np.abs(error_data)), 4)}')
    print(f'Length: {len(error_data)}')
    print('')

    # title = f'{FSR_dir} - Stability Error - JFF(5.00lbf)(Error < 50)'
    title = graph_title
    plt.plot(error_data, 'bo--')
    plt.xlabel('Actuation #')
    plt.ylabel('Percent Error (%)')
    plt.title(title)
    plt.show()

try:
    os.system('clear')
except Exception: 
    os.system('cls')


# Analyze single file
# FSR_dir = 'FSR_S4'
# file_name = 'FSR_S4_4.00lbf' + '.csv'
# stability_graph(FSR_dir, file_name)

# Analysis for FSR S4
names = ["4.00", "4.25", "4.50", "4.75", "5.00", "5.25", "5.50", "5.75", "6.00", "6.25", "6.50", "6.75", "7.00", "7.25", "7.50", "7.75", "8.00", "8.25", "8.50", "8.75", "9.00"]

for i in names:
    FSR_dir = "FSR_S4"
    file_name = f"FSR_S4_{i}lbf"
    full_filename = file_name + ".csv"
    graph_title = f"{FSR_dir} - Stability Error - {i} lbf"
    print(f"Force: {i}")
    stabilityerror_graph(FSR_dir, full_filename, graph_title)