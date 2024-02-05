import matplotlib.pyplot as plt

# Define the function x(n)
def x(n):
    return 4 * n + 1

# Generate values for n from 1 to 25
n_values = list(range(1, 26))

# Compute corresponding x(n) values
x_values = [x(n) for n in n_values]

# Create the stem plot
plt.stem(n_values, x_values, linefmt='-', markerfmt='o', basefmt=' ')

# Highlight points at n=16 and n=23 with different colors
plt.stem([16], [x(16)], linefmt='r-', markerfmt='ro', basefmt=' ')
plt.stem([23], [x(23)], linefmt='r-', markerfmt='ro', basefmt=' ')

# Annotate the highlighted points without arrows
plt.text(16, x(16), f'({16}, x({16}))', ha='right', va='bottom', color='r')
plt.text(23, x(23), f'({23}, x({23}))', ha='right', va='bottom', color='r')

# Set labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot of x(n) = 4n + 1')

# Show the plot

plt.savefig('a_plot.png', dpi = 300, bbox_inches = 'tight')

