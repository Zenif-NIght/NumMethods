import math
import numpy as np
import matplotlib.pyplot as plt


def odeEuler(x,y,h, xGiven, Deriv):
    
    dydx = Deriv(x, y)
    ynew = y + dydx * h
    xnew = x + h
    return xnew, ynew

def functionFall(v):
    return 9.81 - 0.0025 * v**2

odeEuler(0,2000,5)