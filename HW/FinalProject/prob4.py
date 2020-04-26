import matplotlib.pyplot as plt
import numpy as np
import random


def randomSearch(n,function,isConstr):
    x=0
    y=0
    # the random point must be in the constraints 
    while not isConstr(x,y):
        x = 10*random.random()
        y = 10*random.random()
    iter =0
    lastMax =0 #-sys.maxsize
    difrence = 0
    xList =[x]
    yList =[y]

    # keep going tell it reaches n
    while iter <=n:
        xTest =x + difrence*random.random()             
        yTest =y + difrence*random.random() 

        curVal = function(xTest,yTest)
        # print("Test: ",isConstr(xTest,yTest),"(",xTest,",",yTest,")")

        # if the new value is bigger then the lastMax
        # and check if it works in the Solution Space
        if lastMax <curVal and isConstr(xTest,yTest):
            # print("Inter: ",iter," lastMax: ",lastMax,"> curVal: ",curVal )
            difrence =abs( lastMax - curVal)
            # save this point
            x =xTest
            y =yTest
            # update the (x,y)
            yList.append(y)
            xList.append(x)
            lastMax = curVal

        iter +=1
    print("The optimil Value: (",x,",",y,")")
    # print("The Value is Constrained: ", isConstr(x,y))
    # plt.plot(xList,yList,color='red', label="randWalk")
    # plt.show()
    return x,y,xList,yList

def isConstrFun4(x,y):
    # x2 + y2 ≤ 4,
    # x − y ≤ 0,
    # x ≥ 0.5,
    # y ≥ 0.

    if x**2 + y**2 <= 4 and x - y <= 0 and x >= 0.5 and y >= 0:
        return True
    else:
        return False


def fun(x,y):
    return 3*x+y

xi,yi,xLtempi,yLtempi = randomSearch(1000000,fun,isConstrFun4) 
plt.plot(xLtempi,yLtempi,color="red", label="randWalk")
plt.scatter(xi,yi,color="red", label="randWalk")
plt.show()

for i in range(1,100):
    x,y,xLtemp,yLtemp = randomSearch(10000,fun,isConstrFun4) 
    cerColer =np.random.rand(3,)
    plt.plot(xLtemp,yLtemp,color=cerColer, label="randWalk")
    plt.scatter(x,y,color=cerColer, label="randWalk")


plt.show()
# randomSearch(1000000,fun,isConstrFun4) 

