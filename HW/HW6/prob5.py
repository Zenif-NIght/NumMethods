import math
import numpy as np
import matplotlib.pyplot as plt

#GlobalVars
c = 0  # Damping
k = 0  # Spring Const
m = 0  # Mass
def funAccl(v, x):
    return -(c*v + k*x) / m
def velos(v):
    return v


def rungeKuttaMethod(dim1,dim2,step,endTime, fun1,fun2):

    time = [0]

    dim1List = [dim1]
    dim2List = [dim2]

    i = 0
    while time[-1] < endTime:
        #F1
        vF1 = fun1(dim1List[i],dim2List[i])
        pF1 = fun2(dim1List[i])

        #F2
        vF2 = fun1(dim1List[i]+(1/2)*step * vF1, dim2List[i]+(1/2)*step * pF1)
        pF2 = fun2(dim1List[i]+(1/2)*step * vF1)
        

        #F3
        vF3 = fun1(dim1List[i]+(1/2)*step * vF2, dim2List[i]+(1/2)*step * pF1)
        pF3 = fun2(dim1List[i]+(1/2)*step * vF2)


        #F4
        vF4 = fun1(dim1List[i]+step * vF3, dim2List[i] + step * pF1)
        pF4 = fun2(dim1List[i]+step * vF3)

        dim1List.append( dim1List[i] + (vF1+2*(vF2+vF3)+vF4)*step/6)
        dim2List.append(  dim2List[i] + ( pF1+2*(pF2+pF3)+pF4)*step/6)

        time.append(i*step)
        i += 1

    plt.plot(time,dim2List,color='green', label="dim2List")
    plt.ylabel("Position (m)",color='green')
    # plt.legend()
    plt.xlabel("Time (s)")
    plt.twinx()
    plt.plot(time,dim1List,color='red', label="dim1List")
    plt.ylabel("Velocity (m/s)",color ="red")
    plt.title("dim2List and dim1List Vs Time \"Runge Kutta Method\"")
    # plt.legend()
    print("Final Velocity: ",dim1List[-1])
    print("Runge Kutta Method: the object reaches Position: ",dim2List[-2],"m  at the time: ",time[-2],"s")
    plt.show()
    return 


def eulerMethod (dim1,dim2,step,endTime,fun1,fun2):

    time = [0]
    
    dim1List = [dim1]
    dim2List = [dim2]
    i = 0
    while time[-1] < endTime:
        
        dim1List.append( dim1List[i] + fun1(dim1List[i],dim2List[i])*step)
        dim2List.append(  dim2List[i] +fun2(dim1List[i])*step)
        time.append(i*step)
        i += 1

    plt.plot(time,dim2List,color='green', label="dim2List")
    plt.ylabel("Position",color='green')
    # plt.legend()
    plt.xlabel("Time (s)")
    plt.twinx()
    plt.plot(time,dim1List,color='red', label="dim1List")
    plt.ylabel("Velocity",color ="red")
    plt.title("Position and Velocity Vs Time \"Euler Method\"")
    # plt.legend()
    plt.show()
    print("Final dim1List: ",dim1List[-1])
    print("Euler Method: the object reaches Position: ",dim2List[-2],"m  at the time: ",time[-2],"s")
    
    return 

# 5.b
c = 3   # Damping
k = 12  # Spring Const
m = 10  # Mass

# 5.b.i
eulerMethod(0, 1, .5, 15, funAccl,velos)
eulerMethod(0, 1, .01, 15, funAccl,velos)
# 5.b.ii
rungeKuttaMethod(0, 1, .5,15, funAccl,velos)
rungeKuttaMethod(0, 1, .01, 15, funAccl,velos)

# 5.c
c = 50  # Damping
k = 12  # Spring Const
m = 10  # Mass

# 5.b.i

eulerMethod(0, 1, .5, 15, funAccl,velos)
eulerMethod(0, 1, .01, 15, funAccl,velos)

# 5.b.ii
rungeKuttaMethod(0, 1, .5, 15, funAccl,velos)
rungeKuttaMethod(0, 1, .01,15, funAccl,velos)