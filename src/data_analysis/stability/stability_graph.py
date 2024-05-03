import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

def plot_histograms(FSR_dir):
    # Get list of CSV files
    data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
    files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

    # Extract force values from file names using regular expressions
    force_values = []
    for file in files:
        match = re.search(r'\((\d+\.\d+)lbf\)', file)
        if match:
            force_values.append(float(match.group(1)))
        else:
            print(f"Warning: Unable to extract force value from file name: {file}")

    # Sort files based on force values
    files_sorted = [file for _, file in sorted(zip(force_values, files))]

    # Plot histograms
    for file in files_sorted:
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.suptitle('Histogram of Percent Error (%)', fontsize=16, y=0.95)

        file_path = os.path.join(data_path, file)
        df = pd.read_csv(file_path)
        df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages

        sns.histplot(df['Percent Error (%)'], bins=20, kde=True, ax=ax, color='skyblue', edgecolor='black')
        force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
        force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
        ax.set_title(f"Force: {force} lbf", fontsize=14)
        ax.set_xlabel('Percent Error (%)', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.tick_params(axis='both', which='major', labelsize=10)

        plt.tight_layout()
        plt.show()

FSR_dir = 'FSR_S1'
plot_histograms(FSR_dir)