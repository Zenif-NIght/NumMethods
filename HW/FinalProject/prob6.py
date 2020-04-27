import matplotlib.pyplot as plt
import numpy as np
x =[0.2, 0.4, 1.0, 1.5 ]
y =[0.8, 1.5, 0.8, 0.35]

plt.scatter(x,y)
plt.show()

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

e =(e/(n-2))**0.5# square Root
print("Standard Error: ",e)

r = r/(n)
print("Correlation Coefficient r: ",r)

print ("(sy/sx)*r: ",(sy/sx)*r," == m:", m)
if (sy/sx)*r == m:
    print(True)
else:
    print(False)

plt.scatter(x, y) 
y_values = [x[0]*m+c, x[len(x)-1]*m+c]
x_values = [x[0], x[len(x)-1]]

plt.plot(x_values, y_values,color='red')
plt.show()
