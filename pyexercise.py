import sympy as sy
import numpy as np

def fun_1( 1206226 ):
    ans = hex(1206226)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.(1/2*(sqrt(pi)))exp(-x**2), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[3,1,5,9,8], [4,7,6,0,2]] )
    b = np.array([13,32,43,64,18])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    print('Hexadecimal representation of %d is %s'%( 1206226, fun_1( 1206226) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
