import numpy as np
import matplotlib.pyplot as plt

# Read data from file
data = np.loadtxt('values.dat')

# Generate stem plot
plt.figure(figsize=(10, 5))

# Plot stem plot
markerline, stemlines, baseline = plt.stem(range(len(data)), data, linefmt='b-', markerfmt='bo', basefmt='r-', label='Stem Plot')
plt.setp(markerline, color='blue')  # Set marker color to blue
plt.setp(stemlines, color='blue')   # Set stem color to blue

# Plot scatter plot with increased marker size
plt.scatter(range(len(data)), data, color='red', marker='o', label='Scatter Plot', s=100)

plt.title('Stem and Scatter Plot of y(n)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.legend()
plt.show()

