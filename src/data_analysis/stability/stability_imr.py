import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def stability_graph(FSR_dir, file_name):
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file_name)
    
    df = pd.read_csv(file_path, index_col = False)
    
    resistance_data = []
    for index, row in df.iterrows():
        resistance_data.append(np.abs(row.iloc[1]))

    x_bar = round(np.sum(resistance_data)/len(resistance_data))
    
    print(x_bar)

    print('')
    print(f'Average Resistance: {round(np.average(np.abs(resistance_data)))}')
    print(f'Maximum Resistance: {np.max(np.abs(resistance_data))}')
    print(f'Minimum Resistance: {np.min(np.abs(resistance_data))}')
    print(f'Standard Deviation: {round(np.std(np.abs(resistance_data)), 4)}')
    print(f'Length: {len(resistance_data)}')
    print('')



    title = f'{FSR_dir} - IMR Chart - JFF(5.00lbf)'
    plt.plot(resistance_data, 'bo--')
    plt.xlabel('Actuation #')
    plt.ylabel('Resistance ($\Omega$)')
    plt.title(title)
    plt.show()

# os.system('clear')
os.system('cls')
FSR_dir = 'FSR_S2'
file_name = 'FSR_S2_Stability(5.00lbf)' + '.csv'
stability_graph(FSR_dir, file_name)