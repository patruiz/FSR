import sympy as sym

def calc_uncertainty(a, b):
    """
    V_ref = x1
    R1 = x2
    R2 = x3
    V2 = x4
    """
    
    x_1, x_2, x_3, x_4, a, b = sym.symbols('x_1 x_2 x_3 x_4 a b')

    F = (-(.0016*x_1*x_2*x_3)/(a*(x_4-.004*x_3)))**(1/b)

    diff_x1 = F.diff(x_1)
    diff_x2 = F.diff(x_2)
    diff_x3 = F.diff(x_3)
    diff_x4 = F.diff(x_4)

    print(diff_x1)
    print(diff_x2)
    print(diff_x3)
    print(diff_x4)