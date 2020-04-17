import math
import numpy as np
import matplotlib.pyplot as plt

# this functio nreorders the bound if out of order assumed
def testBound(a,b):
    if a > b:
        temp = a
        a = b
        b = temp
        return
    elif a == b:
        print( "Error : the Lower bound is the smae as the upper bound")
        exit(-1)

def trapezoidal(a,b,y,n,funct):
    if n== 0:
        return 0
    testBound(a,b)

    step_x = (b-a) / float(n)

    sumVal = (funct(a,y) + funct(b, y))

    for i in np.arange(1,n,1):
        sumVal += 2 *funct(a + i*step_x,y)

    return (b - a) * sumVal / (2 * n)#step_x*sumVal

# applies the multiple-application trapezoidal rule
# 1st bound a-b 
# then 
# 2nd bound c-c
def dub_trap(a,b,c,d,n,funct):
    sumtot = 0
    if n==0:
        return 0
    step_y = (d - c) / n

    y_list = np.arange(c + step_y, d, step_y)

    sumtot = trapezoidal(a,b,c,n,funct) + trapezoidal(a,b,d,n,funct)

    for i in range(len(y_list)):
        sumtot +=2* trapezoidal(a,b,y_list[i],n,funct) #+ trapezoidal(c,d,y_list[i],n,funct)
 
    return (d - c) * sumtot / (2 * n) #sumtot

def simpsons_1_3(a,b,y,n,funct):
    if n== 0:
        return 0
    testBound(a,b)

    step = float( b - a) /n

    sumVal = 0
    xList = np.arange(a + step, b,step)
    for i in range(len(xList)):
    
        if i == 0 or i % 2 == 0:
            sumVal += 4 * funct(xList[i],y)
        else:
            sumVal += 2 * funct(xList[i],y)

    return ( (b - a) * (funct(a,y) + sumVal + funct( a,y )) / (3*n))
    

# applies the multiple-application Simpson’s 1/3 rule
# 1st bound a-b 
# then 
# 2nd bound c-c
def dub_Simp(a,b,c,d,n,funct):
    sumtot = 0
    if n==0:
        return 0
    step = float(d - c) / n
    y_list = np.arange(c + step, d, step)
    for i in range(len(y_list)):
        if i == 0 or i % 2 == 0:
            sumtot += 4 * simpsons_1_3(a,b,y_list[i],n,funct)
        else:
            sumtot += 2 * simpsons_1_3(a,b,y_list[i],n,funct)       
        

    sumtot +=simpsons_1_3(a,b,c,n,funct)
    sumtot += simpsons_1_3(a,b,d,n,funct)
    return (d - c) *sumtot/ (3*n)
    

CorectVal = (2752/3.0)/(4.0*4) # = 57.33333333



def pob1a(a,b,c,d,max_n,funct):
    print("Starting Problem 1.a  ") 
    # n_list = np.arange(0,max_n,1).tolist()
    y_errorTrap =[]
    y_errorSim =[]
    y_combo =[]
    x_nTrap=[]
    x_nSim = []
    x_nCombo = []
    for n in range(0,max_n):
        curVal = 0
        if n<=0:
            y_errorTrap.append(100)
            y_errorSim.append(100)
            y_combo.append(100)
            x_nCombo.append(n)
            x_nTrap.append(n)
            x_nSim.append(n)
            continue
        if n%2 !=0: #odd
            curVal = dub_trap(a,b,c,d,n,funct)/((b-a)*(d-c))
            y_errorTrap.append(100* abs( curVal - CorectVal )/CorectVal)
            x_nTrap.append(n)
            y_combo.append(100* abs( curVal - CorectVal )/CorectVal)
            x_nCombo.append(n)
            
        else: # even
            curVal = dub_Simp(a,b,c,d,n,funct) /((b-a)*(d-c))
            y_errorSim.append(100* abs( curVal - CorectVal )/CorectVal)
            x_nSim.append(n)
            y_combo.append(100* abs( curVal - CorectVal )/CorectVal)
            x_nCombo.append(n)


    plt.plot(x_nTrap, y_errorTrap,color='blue', label="Percent Trapizodal Error")
    plt.plot(x_nSim, y_errorSim,color='green',label="Percent Simpsons Error")
    plt.plot(x_nCombo, y_combo,color='red',label="Percent Composite Error")
   
    plt.title(" Percent Error vs n")
    plt.ylabel("Percent Error")
    plt.xlabel("n")
    plt.legend()
    plt.show()
    print('Done with Prob1')