import math
import numpy as np
import matplotlib.pyplot as plt

#fun1 is  y = 9.81 -0.0025*x**2
#fun2 is  y = -x
def rungeKuttaMethod(dim1,dim2,step,fun1,fun2):

    time = [0]
    
    dim1List = [dim1]
    dim2List = [dim2]
    dim2_current = dim2

    i = 0
    while dim2_current > 0:
        #F1
        vF1 = fun1(dim1List[i])
        pF1 = fun2(dim1List[i])

        #F2
        vF2 = fun1(dim1List[i]+(1/2)*step * vF1)
        pF2 = fun2(dim1List[i]+(1/2)*step * vF1)
        

        #F3
        vF3 = fun1(dim1List[i]+(1/2)*step * vF2)
        pF3 = fun2(dim1List[i]+(1/2)*step * vF2)


        #F4
        vF4 = fun1(dim1List[i]+step * vF3)
        pF4 = fun2(dim1List[i]+step * vF3)

        dim1List.append( dim1List[i] + (vF1+2*(vF2+vF3)+vF4)*step/6)
        dim2List.append(  dim2List[i] + ( pF1+2*(pF2+pF3)+pF4)*step/6)
        dim2_current = dim2List[i+1]
        time.append(i*step)
        i += 1

    print("Final dim1List: ",dim1List[-1])
    print("Runge Kutta Method: the object reaches Position: ",dim2List[-2],"m  at the time: ",time[-2],"s")
    plt.plot(time,dim2List,color='green', label="dim2List")
    plt.ylabel("Dimension 2",color='green')
    # plt.legend()
    plt.xlabel("Time (s)")
    plt.twinx()
    plt.plot(time,dim1List,color='red', label="dim1List")
    plt.ylabel("Dimension 1 ",color ="red")
    plt.title("Position and Velocity Vs Time \"Runge Kutta Method\"")
    # plt.legend()
    plt.show()
    return 


def eulerMethod (dim1,dim2,step,fun1,fun2):

    time = [0]
    
    dim1List = [dim1]
    dim2List = [dim2]
    dim2_current = dim2

    i = 0
    while dim2_current > 0:
        
        dim1List.append( dim1List[i] + fun1(dim1List[i])*step)
        dim2List.append(  dim2List[i] +fun2(dim1List[i])*step)
        dim2_current = dim2List[i+1]
        time.append(i*step)
        i += 1

    print("Final dim1List: ",dim1List[-1])
    print("Euler Method: the object reaches Position: ",dim2List[-2],"m  at the time: ",time[-2],"s")
    plt.plot(time,dim2List,color='green', label="dim2List")
    plt.ylabel("Dimension 2",color='green')
    # plt.legend()
    plt.xlabel("Time (s)")
    plt.twinx()
    plt.plot(time,dim1List,color='red', label="dim1List")
    plt.ylabel("Dimension 1 ",color ="red")
    plt.title("Position and Velocity Vs Time \"Runge Kutta Method\"")
    # plt.legend()
    plt.show()
    
    return 
