import numpy as np
import matplotlib.pyplot as plt

# Define the range of n
n = np.arange(0, 10)

# Define y[n]
y = np.zeros_like(n)
y[n == 0] = 1
y[n == 1] = -1
y[n == 2] = -0.5
y[n == 3] = 2.5
y[n == 5] = -1

# Plot
plt.stem(n, y, use_line_collection=True)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title(r'Plot of $y[n] = \delta[n] - \delta[n-1] + 2.5\delta[n-3] - 0.5\delta[n-2] - \delta[n-5]$')
plt.grid(True)
plt.show()

