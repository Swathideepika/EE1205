from sympy import symbols, simplify

# Define symbolic variable s
s_L = symbols('s_L')

# Given roots
s1 = -0.4604 - 0.4276j
s2 = -0.4604 + 0.4276j
s3 = -0.1907 + 1.0322j
s8 = -0.1907 - 1.0322j

# Define the given polynomial expression
polynomial_expr = 0.4166 / ((s_L - s1) * (s_L - s2) * (s_L - s3) * (s_L - s8))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
