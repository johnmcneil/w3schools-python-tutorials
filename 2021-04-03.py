# SciPy tutorial
# https://www.w3schools.com/python/scipy_intro.asp
import scipy
from scipy import constants

print(scipy.__version__)

# constants
print(constants.liter)
print(constants.pi)

# optimizers
# procedures that find minimum value of a function, or root of an equation
# algorithms in machine learning are equations that need to be minimized
# with help of given data.
# NumPy can find roots of linear and polynomial equations,
# but can't find roots of nonlinear equations, e.g. x + cos(x)
# for that use SciPy's optimize.root() function
# two arguments: function, x0 (an initial guess of the root)
# returns an object with information on the solution
# solution is under attribute x

# find root of x + cos(x)
from scipy. optimize import root
from math import cos


def eqn(x):
    return x + cos(x)


myroot = root(eqn, 0)

print(myroot.x)
z = cos(myroot.x)
print(z)
print(z + myroot.x)
print(myroot, "\n")

# finding minima
# scipy. optimize.minimize()
# arguments: function, x0 initial guess,
# method: CG, BFGS, Newton-CG, L-BFGS-B, TNC, COBYLA, SLSQP
# callback, called after each iteration of optimization
# optionsL dsip, gtol

# minimize the function x^2 + x + 2 with BFGS:
from scipy.optimize import minimize


def eqn(x):
    return x**2 + x + 2


mymin = minimize(eqn, 0, method='COBYLA')
print(mymin)







































