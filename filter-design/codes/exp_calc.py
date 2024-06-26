import sympy as sp

# Define symbols
s, s_L = sp.symbols('s s_L')

# Given parameters (complex numbers in SymPy format)
s1 = sp.I*(-1.0322) - 0.1907
s2 = sp.I*(-0.4276) - 0.4604
s3 = sp.I*0.4276 - 0.4604
s8 = sp.I*1.0322 - 0.1907
Omega_0 = 0.644
B = 0.1107

# Define the denominator polynomial using SymPy
den = (s_L - s1)*(s_L - s2)*(s_L - s3)*(s_L - s8)

# Given transfer function
Ha_LP_s_L = 0.4166 / den

# Perform substitution
substitution = (s**2 + Omega_0**2) / (B * s)
substituted_expression = Ha_LP_s_L.subs(s_L, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in s:")
print(simplified_expression)
