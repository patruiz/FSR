import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def power_function(x, a, b):
    return a * np.power(x, b)

data = {
    'Initial': {'A': 25494.51322, 'A_SE': 848.34687, 'b': -1.16791, 'b_SE': 0.01934},
    '2ndDayStart': {'A': 19001.27377, 'A_SE': 105.02494, 'b': -1.00721, 'b_SE': 0.00302},
    '2ndDayEnd': {'A': 18185.95344, 'A_SE': 117.52136, 'b': -0.99471, 'b_SE': 0.00353}
}

x_fit = np.linspace(4, 11, 269)

fig, ax = plt.subplots(figsize=(12, 8))

for event, params in data.items():
    y_fit = power_function(x_fit, params['A'], params['b'])
    y_err = np.sqrt((params['A_SE'] * x_fit ** params['b']) ** 2 + 
                    (params['b_SE'] * params['A'] * x_fit ** (params['b'] - 1)) ** 2)
    ax.errorbar(x_fit, y_fit, yerr=y_err, label=event)

ax.set_xlabel('Force (lbf)')
ax.set_ylabel(r'Resistance ($\Omega$)')
ax.set_title('FSR S4 - Comparison of Calibration Curves')
ax.legend(loc='upper center', ncol=3)
ax.grid(True)

plt.show()
