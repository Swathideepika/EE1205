import matplotlib.pyplot as plt

# Read values from the file
values = []
with open("values.txt", "r") as file:
    for line in file:
        # Check if the line contains a valid integer
        try:
            value = int(line.strip())
            values.append(value)
        except ValueError:
            print(f"Ignoring non-numeric line: {line}")

# Plot the graph
n_values = list(range(1, len(values) + 1))
plt.plot(n_values, values, marker='o', linestyle='-')
plt.title('Graph of x(n) = 4n-3')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('c_plot.png', dpi = 300, bbox_inches = 'tight')


