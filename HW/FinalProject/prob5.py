import numpy as np

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

distro = [[0 for j in range(n+1)] for i in range(m+1)]
print(np.matrix(distro))

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



print( "\n",distro[2][1])