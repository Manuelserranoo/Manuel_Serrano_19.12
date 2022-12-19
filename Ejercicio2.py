
from sympy import symbols, simplify
def ecaucion():
    x,y,z = symbols('x,y,z')

    ec = (x + y)**2 + x - y - z

    simplified_equation = simplify(ec)

    return simplified_equation



if __name__ == "__main__":
    print(ecaucion())