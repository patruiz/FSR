import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def power_function(x, a, b):
    return a * np.power(x, b)

data = {
    '1': {'A': 18610.34245, 'A_SE': 117.69955, 'b': -0.9447, 'b_SE': 0.00344},
    '2': {'A': 19780.02869, 'A_SE': 112.43103, 'b': -0.97023, 'b_SE': 0.00308},
    '3': {'A': 18849.23584, 'A_SE': 106.90512, 'b': -0.94597, 'b_SE': 0.00308},
    '4': {'A': 17337.01756, 'A_SE': 106.54469, 'b': -0.90936, 'b_SE': 0.00333},
    '5': {'A': 17347.31507, 'A_SE': 92.1691, 'b': -0.90005, 'b_SE': 0.00288},
    '6': {'A': 17633.23052, 'A_SE': 84.27922, 'b': -0.91141, 'b_SE': 0.0026},
    '7': {'A': 16725.94544, 'A_SE': 79.91529, 'b': -0.88719, 'b_SE': 0.0026},
    '8': {'A': 16716.61174, 'A_SE': 85.1894, 'b': -0.88183, 'b_SE': 0.00275},
    '9': {'A': 15891.7345, 'A_SE': 84.02458, 'b': -0.86186, 'b_SE': 0.00286},
    '10': {'A': 15555.82482, 'A_SE': 85.72963, 'b': -0.84411, 'b_SE': 0.00297}
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
ax.set_title('FSR S3 - Comparison of Calibration Curves')
ax.legend(loc='upper center', ncol=3)
ax.grid(True)

plt.show()
