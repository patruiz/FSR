import os 
import sympy as sym

def uncertainty_propagation(V_ref, R1, R2, V2, a, b):
    """
    V_ref = x1
    R1 = x2
    R2 = x3
    V2 = x4
    """
    
    x_1, x_2, x_3, x_4, A, B = sym.symbols('x_1 x_2 x_3 x_4 A B')

    F = (-(.0016*x_1*x_2*x_3)/(A*(x_4-.004*x_3)))**(1/B)

    partial_derivatives = [F.diff(var) for var in (x_1, x_2, x_3, x_4)]

    subs = {x_1: V_ref, x_2: R1, x_3: R2, x_4: V2, A: a, B:b}

    evaluated_derivatives = [diff.subs(subs) for diff in partial_derivatives]
    
    return evaluated_derivatives

    

print(uncertainty_propagation(24, 1500, 240, -24, 1002, -9123))