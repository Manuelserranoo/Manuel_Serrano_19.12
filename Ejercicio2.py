from sympy import symbols, simplify

# Define the variables
x, y, z = symbols('x, y, z')

# Define the equation
equation = (x + y)**2 + x - y - z

# Simplify the equation
simplified_equation = simplify(equation)

print(simplified_equation)
