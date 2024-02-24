import matplotlib.pyplot as plt

# Read data from the file
with open('values.dat', 'r') as file:
    data = file.readlines()

# Parse data
x = []
y = []
for line in data:
    n, value = line.split()
    x.append(int(n))
    y.append(float(value))

# Plot
plt.stem(x, y, basefmt='k-', use_line_collection=True)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Plot of y[n]')
plt.grid(True)
plt.show()

