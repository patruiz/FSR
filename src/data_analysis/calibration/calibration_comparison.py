import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def power_function(x, a, b):
    return a * np.power(x, b)

data = {
    'Pre-Cond': {'A': 17528.29506, 'A_SE': 109.56891, 'b': -1.01995, 'b_SE': 0.00342},
    'Post-Cond': {'A': 12964.65478, 'A_SE': 82.63371, 'b': -0.90492, 'b_SE': 0.00344},
    'Post-Stability': {'A': 62978.98873, 'A_SE': 367.64105, 'b': -1.45585, 'b_SE': 0.00332}
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
ax.set_title('FSR S1 - Comparison of Calibration Curves')
ax.legend(loc='upper center', ncol=3)
ax.grid(True)

plt.show()
