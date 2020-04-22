import math
import numpy as np
import matplotlib.pyplot as plt

# # http://code.activestate.com/recipes/577647-ode-solver-using-euler-method/
# # (xa, ya) are a know solution point
# # from xa to xb
# # n is the number of steps
# def euler(f, xa, xb, ya, n):
#     # step size
#     step = (xb - xa) / float(n)
#     # x inital
#     x = xa
#     # y intal
#     yb = ya
#     for i in range(n):
#         yb += step * f(x)#f(x, yb)
#         x += step
#     return yb # this is the value at xb    



def fallAccel(v):
    return 9.81 - 0.0025 * v**2

def fallVel(v):
    return -v

# help from:
#  https://github.com/twright/Python-Examples/blob/master/runge-kutta-method.py

def rungeKuttaMethod(xi,yi,step):

    time = [0]
    
    velosList = [xi]
    positionList = [yi]
    y_current = yi

    i = 0
    while y_current > 0:
        #F1
        vF1 = fallAccel(velosList[i])
        pF1 = fallVel(velosList[i])

        #F2
        vF2 = fallAccel(velosList[i]+(1/2)*step * vF1)
        pF2 = fallVel(velosList[i]+(1/2)*step * vF1)
        

        #F3
        vF3 = fallAccel(velosList[i]+(1/2)*step * vF2)
        pF3 = fallVel(velosList[i]+(1/2)*step * vF2)


        #F4
        vF4 = fallAccel(velosList[i]+step * vF3)
        pF4 = fallVel(velosList[i]+step * vF3)

        velosList.append( velosList[i] + (vF1+2*(vF2+vF3)+vF4)*step/6)
        positionList.append(  positionList[i] + ( pF1+2*(pF2+pF3)+pF4)*step/6)
        y_current = positionList[i+1]
        time.append(i*step)
        i += 1

    plt.plot(time,positionList,color='green', label="Position")
    plt.ylabel("Position (m)",color='green')
    # plt.legend()
    plt.xlabel("Time (s)")
    plt.twinx()
    plt.plot(time,velosList,color='red', label="Velocity")
    plt.ylabel("Velocity (m/s)",color ="red")
    plt.title("Position and Velocity Vs Time \"Runge Kutta Method\"")
    # plt.legend()
    print(velosList[-1])
    print("the object reaches Position: ",positionList[-2],"m  at the time: ",time[-2],"s")
    plt.show()
    return 




def eulerMethod (xi,yi,step):

    time = [0]
    
    velosList = [xi]
    positionList = [yi]
    y_current = yi

    i = 0
    while y_current > 0:
        
        velosList.append( velosList[i] + fallAccel(velosList[i])*step)
        positionList.append(  positionList[i] -(velosList[i])*step)
        y_current = positionList[i+1]
        time.append(i*step)
        i += 1
    print(i)
    plt.plot(time,positionList,color='green', label="Position")
    plt.ylabel("Position (m)",color='green')
    # plt.legend()
    plt.xlabel("Time (s)")
    plt.twinx()
    plt.plot(time,velosList,color='red', label="Velocity")
    plt.ylabel("Velocity (m/s)",color ="red")
    plt.title("Position and Velocity Vs Time \"Euler Method\"")
    # plt.legend()
    print("Final Velocity: ",velosList[-1])
    print("the object reaches Position: ",positionList[-2],"m  at the time: ",time[-2],"s")
    plt.show()
    return 


eulerMethod(0,2000,0.001)
# print(euler(functionFall, 0, 38, 0, 36354))
rungeKuttaMethod(0,2000,0.001)