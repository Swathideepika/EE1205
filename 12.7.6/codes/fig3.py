import numpy as np
import matplotlib.pyplot as plt

# Define the expression
def expression(omega, mu):
    return np.sqrt(10**2 + (omega * 2 - 1/(omega * 32*mu))**2)

# Generate omega values
omega_values = np.linspace(0.1, 10, 1000)  # Adjust the range and number of points as needed

# Choose a value for mu (viscosity)
mu_value = 0.1  # Adjust as needed

# Calculate the corresponding y values
y_values = expression(omega_values, mu_value)

# Plot the graph
plt.plot(omega_values, y_values, label=r'$\sqrt{10^2 + \left(\omega \cdot 2 - \frac{1}{\omega \cdot 32\mu}\right)^2}$')
plt.xlabel('Omega')
plt.ylabel('|H(j$\omega$)|')
plt.title('Graph of the amplitude and omega')
plt.legend()
plt.grid(True)
plt.savefig('q_plot.png', dpi = 300, bbox_inches = 'tight')

