import numpy as np
import matplotlib.pyplot as plt

def prob3(x,y):
    print("Starting Prob 3")
    # x = [ 0, 2, 4, 6, 9, 11, 12, 15, 17, 19]
    # y = [ 5, 6, 7, 6, 9, 8 , 7 , 10, 12, 12] 

    x_sum = np.sum(x)
    y_sum = np.sum(y)
    num = 0
    den = 0
    n = len(x)
    for i in range(len(x)):

        num +=n*( x[i]*y[i])
        den += n*x[i]**2

    num =  num - x_sum*y_sum
    den = den - (x_sum)**2  

    m = num / den
    c =( y_sum - m * x_sum)/n

    print ("Slope: ",m,"Y Intersept:", c)
    e=0#[None]*len(x)

    sx = np.std(x)
    sy = np.std(y)
    x_mean = np.mean(x)
    y_mean = np.mean(y)


    r = 0
    for i in range(len(x)):
        # Standard Error Calulation
        ycal=(x[i]*m+c)
        e += (y[i]-ycal)**2

        # Colication Calulation
        zx = (x[i]-x_mean)/sx
        zy = (y[i]-y_mean)/sy
        r += zx*zy


    e =(e/n)**0.5# square Root
    print("Standard Error: ",e)

    r = r/(n)
    print("Correlation Coefficient r: ",r)

    print ("(sy/sx)*r: ",(sy/sx)*r," == m:", m)
    if (sy/sx)*r == m:
        print(True)
    else:
        print(False)

    plt.scatter(x, y) 


    # coralation = 


    y_values = [x[0]*m+c, x[len(x)-1]*m+c]
    x_values = [x[0], x[len(x)-1]]

    plt.plot(x_values, y_values,color='red')
    plt.show()


def prob4(x,y,numofConst):
    # x = [1  , 2  , 3  , 4  , 5  ]
    # y = [2.2, 2.8, 3.6, 4.5, 5.5]
    z = [[None]*numofConst ]*len(x)


    for i in range(len(x)):
        z[i]= [1, i+1,1/(i+1)]

    y = np.matrix(y).transpose()
    print(y)
    z = np.matrix(z)
    print(np.matrix(z))

    zt = z.transpose()
    vMat = zt*z
    print (vMat)
    ansMat = np.linalg.inv(vMat)*zt*y
    print(ansMat)
    return ansMat


if __name__ == "__main__":
    x = [ 0.0, 2.0, 4.0, 6.0, 9.0, 11.0, 12.0, 15.0, 17.0, 19.0]
    y = [ 5.0, 6.0, 7.0, 6.0, 9.0,  8.0,  7.0, 10.0, 12.0, 12.0] 

    # prob3(x,y)

    numofConst =3
    x = [1  , 2  , 3  , 4  , 5  ]
    y = [2.2, 2.8, 3.6, 4.5, 5.5]
    prob4(x,y,numofConst)