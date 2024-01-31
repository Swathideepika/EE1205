import matplotlib.pyplot as plt

# Read values from the file
with open('values.txt', 'r') as file:
    values = [int(line.strip()) for line in file]

# Generate indices for the stem plot
indices = list(range(1, len(values) + 1))

# Plot the stem graph
plt.stem(indices, values, basefmt="k-", linefmt="b-", markerfmt="bo")
plt.title('Stem Graph of x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('a_plot.png', dpi = 300, bbox_inches = 'tight')


