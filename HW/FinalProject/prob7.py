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
    # 1.a < b
    testBound(a,b)

    if (n%2 == 0 or n < 3):
        print("as stated in the Problem statement on prescribed odd (n≥ 3) are alowed")
        print("You picked n = ",n)
        return None
    
    elif (n >= 3): # 2.	prescribed odd number of subintervals n ≥ 3
        sumTot = 0
        step = (b-a)/n
        # 3.multiple-application Simpson’s 1/3 rule on the first n − 3 subintervals
        sumTot += simpsons_1_3(a,b-3*step,n-3,funct)
    
        # 4.Simpson’s 3/8 rule on the last 3 subintervals
        sumTot += simpsons_3_8(b-3*step, b, 3,funct)

        return sumTot 
