import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, linregress

# Define a function to plot histograms with fitted normal curves
def plot_histogram_with_fit(df, column, title, img_dir):
    data = df[column]
    plt.figure(figsize=(10, 6))
    sns.histplot(data, kde=False, color='skyblue', bins=15, stat='density', edgecolor='black')
    mu, std = norm.fit(data)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    plt.title(f"{title} - Histogram and Normal Fit Curve", fontsize=14, fontweight='bold')
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.savefig(img_dir)
    plt.close()

# Define a function to plot box plots
def plot_boxplot(df, title, img_dir):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.savefig(img_dir)
    plt.close()

# Define a function to plot scatter plots with trend lines
def plot_scatter_with_trend(df, x, y, title, img_dir):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x, y=y)
    slope, intercept, r_value, p_value, std_err = linregress(df[x], df[y])
    plt.plot(df[x], intercept + slope*df[x], 'r', label=f'fit: slope={slope:.2f}, intercept={intercept:.2f}')
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(x, fontsize=12)
    plt.ylabel(y, fontsize=12)
    plt.legend()
    plt.savefig(img_dir)
    plt.close()

# Define a function to plot correlation heatmaps
def plot_correlation_heatmap(df, title, img_dir):
    plt.figure(figsize=(10, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title(title, fontsize=14, fontweight='bold')
    plt.savefig(img_dir)
    plt.close()

# Define a function to plot standard deviation vs. stability force
def plot_std_vs_force(df, x, y, title, img_dir):
    std_dev = df.groupby(x)[y].std()
    plt.figure(figsize=(10, 6))
    std_dev.plot(marker='o', linestyle='-', color='blue')
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Stability Force (lbf)', fontsize=12)
    plt.ylabel('Standard Deviation (Ohms)', fontsize=12)
    plt.savefig(img_dir)
    plt.close()

# Main analysis function
def stability_analyze(file_path, img_dir):
    df = pd.read_csv(file_path)
    
    # Example usage of plot functions
    plot_histogram_with_fit(df, 'Resistance (Ohms)', 'Resistance Distribution', os.path.join(img_dir, 'histogram.jpg'))
    plot_boxplot(df[['Resistance (Ohms)', 'Max Resistance (Ohms)', 'Min Resistance (Ohms)']], 'Resistance Box Plot', os.path.join(img_dir, 'boxplot.jpg'))
    plot_scatter_with_trend(df, 'Stability Force (lbf)', 'Resistance (Ohms)', 'Resistance vs. Force Scatter Plot', os.path.join(img_dir, 'scatter.jpg'))
    plot_correlation_heatmap(df, 'Correlation Heatmap', os.path.join(img_dir, 'heatmap.jpg'))
    plot_std_vs_force(df, 'Stability Force (lbf)', 'Resistance (Ohms)', 'Standard Deviation vs. Stability Force', os.path.join(img_dir, 'std_vs_force.jpg'))

# Example of calling stability_analyze with a path and directory
file_path = "/Users/patrickruiz/Desktop/FSR/data/FSR_S4/stability/FSR_S4_6.50lbf.csv"
img_dir = "/Users/patrickruiz/Desktop/FSR/data/FSR_S4/images/FSR_S4_6.50lbf"
stability_analyze(file_path, img_dir)