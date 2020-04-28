import numpy as np




#          0       1      2  x values
#   0_     |   0   |   1  |  i/m values
#   1_ 0-| [[(0, 0), (0, 1)],
#   2_ 1-|  [(1, 0), (1, 1)],
#   3_ 2-|  [(2, 0), (2, 1)]]
#   ^   ^
#   |   |_  j/n values
#   |
#   |_  y values

#            0|.5|1.5|2  x values
#            0| 1| 2 |3  i/m values
#  0   0   [[0| 0| 0 |0] 
#  .5  1    [0| 0| 0 |0]
# 1.5  2    [0| 0| 0 |0]
# 2.5  3    [0| 0| 0 |0]
# 1.5  4    [0| 0| 0 |0]]



def main():
    # n= 4
    # m=4
    # meand ther 4 rect  by 4 rect
    ymax =3
    xmax =2
    n = 2 #
    m = 3

    stepY = ymax/n
    stepX = xmax/m
    print("stepX: ",stepX)
    print("stepY: ",stepY)



    sumVal= 0
    mat = [[0 for j in range(n+1)] for i in range(m+1)]
    print(np.matrix(mat))

    y =np.arange(n).tolist()
    err =0

    for i in range( n):
        y[i] = 0
        a = 0
        for i in range( m):

            sumVal = 0
            for t in range(a) :

                a = err

                y[i] = y[t] 
            # print("\nY[%d]=\t%f", count, y[count])

        print("\n")

    while(a >= err):


        for i in range( n):

            

    return 0




main()