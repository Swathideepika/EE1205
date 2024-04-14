import numpy as np
import matplotlib.pyplot as plt

# Define coefficients
coefficients1 = [8, 0, 8, 0, 1 + 10.0j / 3.0]
coefficients2 = [8, 0, 8, 0, 1 - 10.0j / 3.0]

# Calculate the roots
roots1 = np.roots(coefficients1)
roots2 = np.roots(coefficients2)

# Plot real vs imaginary parts
plt.figure(figsize=(8, 6))
plt.plot(np.real(roots1), np.imag(roots1), 'rx')
plt.plot(np.real(roots2), np.imag(roots2), 'rx')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Pole-Zero Plot')
plt.grid(True)
plt.savefig("../figs/pole.png")
plt.show()
