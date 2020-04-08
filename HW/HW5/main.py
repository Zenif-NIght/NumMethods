import math
import numpy as np
import matplotlib.pyplot as plt



def testBound(a,b):
    if a > b:
        temp = a
        a = b
        b = temp
        return
    elif a == b:
        print( "Error : the Lower bound is the smae as the upper bound")
        exit(-1)

def trapezoidal(a,b,n,funct):
    print("starting trapezoidal")
    if n== 0:
        return 0
    testBound(a,b)

    step = (b-a) / float(n)

    sumVal = 0.5*(funct(a) + funct( b))

    for i in np.arange(1,n,1):
        sumVal += funct(a + i*step)

    return step*sumVal

def simpsons_1_3(a,b,n,funct):
    if n== 0:
        return 0
    testBound(a,b)

    step = ( b - a) /n

    sumVal = 0
    xList = np.arange(a + step, b,step)
    for i in range(len(xList)):
    
        if i == 0 or i % 2 == 0:
            sumVal += 4 * funct(xList[i])
        else:
            sumVal += 2 * funct(xList[i])

    return ( (b - a) * (funct(a) + sumVal + funct( b )) / (3*n))

def simpsons_3_8(a,b,n,funct):
    if n== 0:
        return 0
    testBound(a,b)

    # Interval Size  = step
    step = (( b -  a) / n) 
    sumVal = funct( a) + funct( b)

    for i in range(1, n ): 
        if (i % 3 == 0):
            sumVal = sumVal + 2 * funct( a + i * step)
        else:
            sumVal = sumVal + 3 * funct( a + i * step)
    
    return (( 3 * step) / 8 ) * sumVal 

def prob2Algorithm(a,b,n,funct):

    testBound(a,b)

    if (n == 1 ):
        return trapezoidal(a,b,n,funct)

    elif (n%2 == 0):
        return simpsons_1_3(a,b,n,funct)
    
    elif (n >= 3): # and Odd 
        sumTot = 0
        step = (b-a)/n
        # For the first n−3 n
        sumTot += simpsons_1_3(a,b-3*step,n-3,funct)
    
        # Last three n
        sumTot += simpsons_3_8(b-3*step, b, 3,funct)

        return sumTot 
    else:
        print("you picked a crazy number for 'n'.... like 3")
        exit(-1)

def qstep(a,b,funct,tolError,fa, fc, fb):
    c = (a+b)/2
    h1 = b -a
    h2 = h1/2
    fd = funct((a+c)/2)
    fe = funct((c + b)/2)
    I1 = h1/6 * (fa + 4 * fc + fb) #(Simpson’s 1/3 rule)
    I2 = h2/6 * (fa + 4 * fd + 2 * fc + 4 * fe + fb)
    if abs( I2 - I1) <= tolError: # (terminate after Boole’s rule)
        I = I2 + (I2 - I1)/15

    else: # (recursive calls if needed)
        Ia = qstep(a, c, funct,tolError, fa, fd, fc)
        Ib = qstep(c, b, funct, tolError, fc, fe, fb)
        I = Ia + Ib

    return I

def adaptiveQuadrature(a,b,funct):
    testBound(a,b)
    fa = funct(a)
    fb = funct(b)
    c = (a+b)/2
    fc = funct(c)
    qstep(a,b,funct,0.000001, fa, fc, fb)


def func1(x):
    x = float(x)
    return (x**0.1)*(1.2-x)*(1.0-math.exp(20.0*(x-1.0)))

if __name__ == "__main__":
    print("Starting Application...")
    # prob2Algorithm(0,1,3,func1)
    n_max = 100 
    y_errorTrap = [None]*n_max
    y_errorSim = [None]*n_max
    x_nVals = [None]*n_max

    TrueVal = 0.602298

    for n in range(0,n_max):
        if n == 0:
           y_errorTrap[n] =0
           y_errorSim[n] =0 
           continue
        x_nVals[n] = n

        # test Prob 1
        y_errorTrap[n] = TrueVal- trapezoidal(0,1,n,func1)

        # test Prob 2
        y_errorSim[n] = TrueVal- prob2Algorithm(0,1,n,func1)
        
    # test Prob 3
    adaptiveQuadrature(0,1,func1)
    
    plt.plot(x_nVals, y_errorTrap,color='blue',label="Trapizodal Error")
    
    plt.plot(x_nVals, y_errorSim,color='green',label="Simpsons Error")
    plt.title("Trapizodal and Simpsons Error")
    plt.legend()
    plt.show()

    def fenfun(x):
        return x**2
    print(trapezoidal(0,1,100,fenfun))
    