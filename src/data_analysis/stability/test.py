import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

names = ["4.00", "4.25", "4.50", "4.75", "5.00", "5.25", "5.50", "5.75", "6.00", "6.25", "6.50", "6.75", "7.00", "7.25", "7.50", "7.75", "8.00", "8.25", "8.50", "8.75", "9.00"]

# Clear the console
try:
    os.system("clear")
except Exception:
    os.system("cls")

for i in names:
    FSR_dir = "FSR_S4"
    file_name = f"FSR_S4_{i}lbf"
    full_filename = file_name + ".csv"
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability_error', full_filename)

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        continue

    ohms = np.array(df["Resistance (Ohms)"])

    print("\n")
    print(f"Force: {i}")
    print(f"Sample Size: {len(ohms)}")
    print(f"Max: {round(np.max(ohms))}")
    print(f"Min: {round(np.min(ohms))}")
    print(f"Range: {round(np.max(ohms) - np.min(ohms))}")

    # Create a figure
    plt.figure(figsize=(12, 6))

    # Title for the entire figure
    plt.suptitle(f"Force: {i}", fontsize=18, fontweight='bold', color='black')

    # Histogram with curve fit
    plt.subplot(1, 2, 1)
    sns.histplot(ohms, kde=False, color='skyblue', bins=15, stat='density', edgecolor='black')
    
    mu, std = norm.fit(ohms)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    
    plt.plot(x, p, 'k', linewidth=2)
    title = "Histogram and Normal Fit Curve"
    plt.title(title, fontsize=14, fontweight='bold', color='black')
    plt.xlabel('Resistance (Ohms)', fontsize=12)
    plt.ylabel('Density', fontsize=12)

    # Individual Values Chart
    plt.subplot(2, 2, 2)
    plt.plot(ohms, marker='o', linestyle='-', color='blue', label='Individual Values')
    plt.xlabel('Sample Index', fontsize=12)
    plt.ylabel('Resistance (Ohms)', fontsize=12)
    plt.title('Individual Values Chart', fontsize=14, fontweight='bold', color='black')
    
    # Calculate UCL and LCL for Individual Values
    mr = np.abs(np.diff(ohms))
    mr_average = np.mean(mr)
    mr_std = np.std(mr)
    ucl = ohms.mean() + 3 * mr_std
    lcl = ohms.mean() - 3 * mr_std
    plt.axhline(ucl, color='green', linestyle='--', label='UCL')
    plt.axhline(lcl, color='red', linestyle='--', label='LCL')
    plt.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=3)

    # Moving Range Chart with Average
    plt.subplot(2, 2, 4)
    plt.plot(np.arange(1, len(mr) + 1), mr, marker='o', linestyle='-', color='red', label='Moving Range')
    plt.axhline(mr_average, color='black', linestyle='--', label='Average')
    plt.xlabel('Sample Index', fontsize=12)
    plt.ylabel('Moving Range (Ohms)', fontsize=12)
    plt.title('Moving Range Chart', fontsize=14, fontweight='bold', color='black')
    plt.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2)

    plt.tight_layout()
    plt.show()
