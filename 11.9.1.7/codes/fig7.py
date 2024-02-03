import matplotlib.pyplot as plt

# Define x values
x_values = list(range(0, 26))

# Calculate y values based on the relationship y = 4x + 1
y_values = [4 * x + 1 for x in x_values]

# Plot the stem graph
plt.stem(x_values, y_values, basefmt='k-', linefmt='b-', markerfmt='bo', use_line_collection=True)

# Highlight points for x = 16 and x = 23 with different colors
highlight_x = [16, 23]
highlight_y = [4 * x + 1 for x in highlight_x]
plt.stem(highlight_x, highlight_y, linefmt='r-', markerfmt='ro', label='Highlighted Points', use_line_collection=True)

# Add text annotation above the highlighted points
for i, txt in enumerate(highlight_x):
    plt.annotate(f'({txt})', (txt, highlight_y[i]), textcoords="offset points", xytext=(0, 10), ha='center', va='bottom')

# Set y-axis ticks
plt.yticks([1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

# Add labels and legend
plt.xlabel('n')
plt.ylabel('x(n)')
plt.legend()

# Show the plot
plt.savefig('a_plot.png', dpi=300, bbox_inches='tight')

