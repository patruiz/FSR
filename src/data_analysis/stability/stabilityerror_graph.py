import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def stability_graph(FSR_dir, file_name):
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability_error', file_name)
    
    df = pd.read_csv(file_path, index_col = False)
    
    error_data = []
    for index, row in df.iterrows():
        error_data.append(np.abs(row.iloc[3]))

    print('')
    print(f'Average Error: {round(np.average(np.abs(error_data)), 4)}')
    print(f'Maximum Error: {np.max(np.abs(error_data))}')
    print(f'Minimum Error: {np.min(np.abs(error_data))}')
    print(f'Standard Deviation: {round(np.std(np.abs(error_data)), 4)}')
    print(f'Length: {len(error_data)}')
    print('')

    title = f'{FSR_dir} - Stability Error - JFF(5.00lbf)(Error < 50)'
    plt.plot(error_data, 'bo--')
    plt.xlabel('Actuation #')
    plt.ylabel('Percent Error (%)')
    plt.title(title)
    plt.show()

# os.system('clear')
os.system('cls')
FSR_dir = 'FSR_S2'
file_name = 'FSR_S2_Stability(5.00lbf)' + '.csv'
stability_graph(FSR_dir, file_name)