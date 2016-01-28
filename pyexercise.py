import sympy as sy
import numpy as np

def fun_1( my_id ):
    ans = hex(my_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(-2*x**3), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[3,1,5,9,8,2,6,7,1,3], [1,2,4,7,6,2,4,6,9,3],[9,7,4,2,5,8,3,5,7,9],[4,2,6,8,7,4,6,9,1,3],[2,6,8,0,4,6,9,3,1,7],[7,6,0,4,2,9,4,9,7,1],[6,9,0,3,1,0,5,3,8,4],[0,5,8,4,8,3,2,1,6,8],[7,0,8,5,1,4,6,8,0,4],[2,6,9,0,5,3,6,8,2,5]] )
    b = np.array([21,48,33,80,76,90,51,46,55,79])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    my_id = 1206226
    print('Hexadecimal representation of %d is %s'%( my_id, fun_1(my_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
