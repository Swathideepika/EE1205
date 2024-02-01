import matplotlib.pyplot as plt

# Read values from the text file
with open("values.txt", "r") as file:
    values = [int(line.strip()) for line in file]

# Plot the stem graph
plt.stem(range(1, 26), values, basefmt='k-', use_line_collection=True)

# Highlight points for n = 17 and n = 24 in different colors
plt.stem([17, 24], [values[16], values[23]], linefmt='r-', markerfmt='ro', label='n = 17')
plt.stem([17, 24], [values[16], values[23]], linefmt='g-', markerfmt='go', label='n = 24')

# Add labels and legend
plt.xlabel('n')
plt.ylabel('x(n)')
plt.legend()

# Show the plot
plt.savefig('a_plot.png', dpi = 300, bbox_inches = 'tight')


