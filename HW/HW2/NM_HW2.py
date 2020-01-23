#  Authored by Christopher Allred 
#  A02233404
#  Numerical Methods
#  Spring 2020
'''
Homework 2 is due online through Canvas in PDF format by 11:59PM on Thursday January 23. 
These problems should be solved with programming, by calling func- tions named “Bisection”, 
“FalsePosition”, “NewtonRaphson”, and “Secant”. You are required to submit code for all 
functions and/or subroutines built to solve these problems, which is designed to be easy to 
read and understand, in your chosen programming language, and which you have written yourself.
 The text from your code should both be copied into a single PDF file submitted on canvas.
  Your submitted PDF must also include responses to any assigned questions, which for problems
   requiring programming should be based on output from your code. For example, if you are 
   asked to find a numerical answer to a problem, the number itself should be included in
    your submission.
'''
## use pip3 to install
import numpy as np
import math
import matplotlib.pyplot as plt 
import BisectionMethod
import FalsePosition
import NewtonRaphson


def graph(formula, x_arange):  
    # https://stackoverflow.com/a/14000631
    x = np.array(x_arange)  
    y = formula(x)
    plt.plot(x, y)  
    minV =np.min(x_arange,0)
    maxV =np.max(x_arange,0)
    plt.plot((maxV,minV),(0,0))
    plt.show()

# 1. Determine the real root of f(x)=x**5 −10*x**4 +46*x**3 −90*x**2 +85*x−31
# (a) Graphically.
# (b) Using the bisection method to determine the root with εs = 10%. Employ the initial guesses of xl = 0.5 and xu = 1.0.
# (c) Perform the same computation as in (b) but use the false position method and εs = 0.2%.
def fun1(x):
    return  (x**5) - 10*(x**4) + 46*(x**3) - 90*(x**2) + 85*x - 31

def prob1():
    # (a) Graphically.
    
    graph(fun1,np.arange(0.5,1,0.0001))
    # 0.8858
    
    # (b) Using the bisection method to determine the root with εs = 10%. 
    # Employ the initial guesses of xl = 0.5 and xu = 1.0.
    xl = 0.001
    xu = 1.0
    es = 0.01
    imax =  15
    xIntersect_1B = BisectionMethod.Bisect(fun1,xl, xu, es, imax)
    # 0.881923614501953 is was the root approximation

    # (c) Perform the same computation 
    # as in (b) but use the false position 
    # method and εs = 0.2%.
    es = 0.002
    xIntersect_1C = FalsePosition.FalsePos(fun1,xl, xu, es, imax)
    # 0.883263253774883 the root approx
    return


# 2. Determine the lowest real root of f(x) = −3x**3 + 20x**2 − 20*x − 12
# (a) Graphically.
# (b) Using the bisection method to determine the lowest root with εs = 2%. Employ the initial guesses of xl = −1 and xu = 0.
# (c) Perform the same computation as in (b) but using the false position method.
def fun2(x):
    return   -3*(x**3) + 20*(x**2) - 20*x - 12

def prob2():
    # (a) Graphically.
    graph(fun2,np.arange(-1,6,0.1))
    # x1_intersept = - 0.4153
    # x2_intersept = 1.8281
    # x3_intersept = 5.2515
    
    
    # (b) Using the bisection method to determine 
    # the LOWEST root with εs = 2%. Employ the initial 
    # guesses of xl = −1 and xu = 0.
    xl = -1
    xu = 0
    es = 0.02
    imax =  15
    x1_intersept_B = BisectionMethod.Bisect(fun2,xl, xu, es, imax)
    # -0.416046142578125

    # (c) Perform the same computation as in (b) but using the false 
    # position method.
    xl = -0.5
    xu =-0.3
    es = 0.002
    x1_intersept_C = FalsePosition.FalsePos(fun2,xl, xu, es, imax)
    # -0.4160760388199209
    return


# 3. Textbook problem 5.13.
# The velocity y of a falling parachutist is given by
'''
v = ((g*m)/c)*(1-e^(-(c/m)t) )
where g = 9.81. For a parachutist with a drag coeffi cient
c = 15 kg/s, compute the mass m so that the velocity is y = 36 m/s
at t = 10 s. Use the false-position method to determine m to a level
of es = 0.1%.
'''
def fun3(m):
    # return the mass
    g = 9.81
    c = 15
    t = 10
    # v = 36
    return  ((g*m)/c)*(1-math.exp(-(c/m)*t)) -36

def prob3():

    imax = 15
    xLower = 20
    xUpper = 100
    es = 0.01
    x1_intersept = FalsePosition.FalsePos(fun3,xLower, xUpper, es, imax)
    # 59.95967357510667

# 4. Determine the real roots of f(x) = 0.5*(x**3) − 4*(x**2) + 8*x − 1 
# (a) Graphically.
# (b) Using the Newton-Raphson method to within εs = 0.01%.

def fun4(x):
    return  0.5*(x**3) - 4*(x**2) + 8*x - 1 
def fun4Der(x):
    return 3*0.5*(x**2) - 2*4*(x) + 8 

def prob4():
    # (a) Graphically.
    graph(fun4,np.arange(0.0,5,0.01))
    # 0.1337
    
    # (b) Using the Newton-Raphson method to within εs = 0.01%.
    XGuess = 0
    imax = 15
    errorThresh = 0.01/100
    NewtonRaphson.newtRap(fun4,fun4Der,XGuess,errorThresh,imax)
    # 0.1338017374909775

    
# 5. Determine all roots of f(x) = −3x3 + 20x2 − 20x − 12
# (a) Using the Secant method to a value of εs corresponding to three significant figures.



if __name__ == '__main__':
    # prob1()

    # prob2()

    # prob3()

    prob4()
    
