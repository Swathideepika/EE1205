import numpy as np

#define coefficients
coefficients = [8, 0, 8, 0, 1+10.0j/3.0]

# Calculate the roots
roots = np.roots(coefficients)

# Print the roots
print("The roots of the polynomial are:")
for root in roots:
    print(root)
    
#define coefficients
coefficients = [8, 0, 8, 0, 1-10.0j/3.0]

# Calculate the roots
roots = np.roots(coefficients)

# Print the roots
for root in roots:
    print(root)
