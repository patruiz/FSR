import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def power_function(x, a, b):
    return a * np.power(x, b)

data = {
    'Pre-Cond-1': {'A': 21806.88095, 'A_SE': 152.65029, 'b': -1.00784, 'b_SE': 0.00382},
    'Post-Cond-1': {'A': 16350.46813, 'A_SE': 95.63404, 'b': -0.88515, 'b_SE': 0.00316},
    'Pre-Cond-2': {'A': 26459.3715, 'A_SE': 119.01181, 'b': -1.06083, 'b_SE': 0.00247},
    'Post-Cond-2': {'A': 21939.00353, 'A_SE': 245.64123, 'b': -0.99305, 'b_SE': 0.0061}
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
ax.set_title('FSR S2 - Comparison of Calibration Curves - 2')
ax.legend(loc='upper center', ncol=3)
ax.grid(True)

plt.show()
