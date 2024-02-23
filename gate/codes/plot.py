import numpy as np
import matplotlib.pyplot as plt

# Define the sequence function y[n]
def y_sequence(n):
    return (1 if n == 0 else 0) - (1 if n == 1 else 0) + 2.5*(1 if n == 3 else 0) - 0.5*(1 if n == 2 else 0) - (1 if n == 5 else 0)

# Calculate y[3]
y_3 = y_sequence(3)

# Plot the sequence
n_values = np.arange(0, 10)  # Adjust range as needed
y_values = [y_sequence(n) for n in n_values]

plt.stem(n_values, y_values, use_line_collection=True)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Plot of y[n]')
plt.grid(True)
plt.show()

