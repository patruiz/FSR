import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def power_function(x, a, b):
    return a * np.power(x, b)

data = {
    'Pre-Stability-1': {'A': 37255.92516, 'A_SE': 144.68514, 'b': -1.13455, 'b_SE': 0.00214},
    'Post-Stability-1': {'A': 31615.54399, 'A_SE': 149.47498, 'b': -1.08958, 'b_SE': 0.0026},
    'Post-Stability-2': {'A': 22121.19563, 'A_SE': 96.616, 'b': -0.9704, 'b_SE': 0.00238},
    'Post-Stability-3': {'A': 21125.94518, 'A_SE': 96.87531, 'b': -0.96352, 'b_SE': 0.0025}
}

x_fit = np.linspace(4, 11, 100)

fig, ax = plt.subplots(figsize=(12, 8))

for event, params in data.items():
    y_fit = power_function(x_fit, params['A'], params['b'])
    y_err = np.sqrt((params['A_SE'] * x_fit ** params['b']) ** 2 + 
                    (params['b_SE'] * params['A'] * x_fit ** (params['b'] - 1)) ** 2)
    ax.errorbar(x_fit, y_fit, yerr=y_err, label=event)

ax.set_xlabel('Force (lbf)')
ax.set_ylabel(r'Resistance ($\Omega$)')
ax.set_title('FSR S3 - Comparison of Calibration Curves')
ax.legend(loc='upper center', ncol=3)
ax.grid(True)

plt.show()
