#  Authored by Christopher Allred 
#  A02233404
#  Numerical Methods
#  Spring 2020

#################################
# 2.  Textbook problem 2.26.(Textbook may have a typo labeling 
# this as problem 20.26, see page 53

# 20.26 The height of a small rocket y can be calculated as a function
# of time after blastoff with the following piecewise function:
# y = 38.1454t + 0.13743 t**3                                            0 <= t <= 15
# y = 1036 + 130.909(t - 15) + 
#       6.18425(t - 15)**2 - 0.428(t - 15)**3                             15 <= t < 33
# y = 2900262.468(t -33)-16.9274(t -33)**2 + 0.41796(t -33)**3            t > 33

# Develop a well-structured pseudocode function to compute y as a
# function of t. Note that if the user enters a negative value of t or if
# the rocket has hit the ground (y # 0) then return a value of zero
# for y. Also, the function should be invoked in the calling program
# as height(t). Write the algorithm as (a) pseudocode, or (b) in
# the high-level language of your choice.
import matplotlib.pyplot as plt

def height(t):

    h = None

    if t < 0 :
        print( "Silly you, space travel these days only happens in the forward direction")
        return 0

    elif  0 <= t and t <= 15 :
        h = 38.1454*t + 0.13743 * t**3 

    elif 15 <= t and t < 33:
        h =  1036 + 130.909*(t - 15) +  6.18425*(t - 15)**2 - 0.428*(t - 15)**3  
    elif t >= 33:
        h =  2900 - 62.468*(t -33) - 16.9274*(t -33)**2 + 0.41796*(t -33)**3 
        if  ( - 62.468 - 2*16.9274*(t-33) + 3*0.41796*(t-33)**2) >= 0:
            #if the derivitve >0 the rocket is landed
            h = 0
    else:
        # Check Error
        print( "Wow,We dont know what happend to your rocket, but some how the value t:" + str(t) + " got you here! ¯\\_(ツ)_/¯ " )         
        return None

    if h <0:
        h = 0
    
    return h

#################################
'''
 3.a)  The following infinite series can be used to approximateex:
  e**x= 1 + x + (x**2)/2!+(x**3)/3!+···+(x**n)/n!+···
 (i) Prove that this Maclaurin series expansion is a special case of the Taylor series expansion
    (Eq. (4.7)in text) with xi =0 and h=x.
Taylor: f(xi )= f(xi)+f'(xi)h + (f''(xi)h**2)/2! + (f'3'(xi)h**3)/3! + ... + (f'n'(xi)h**n)/n! + R
Maclaurin:   e**x= 1 + x + (x**2)/2!+(x**3)/3!+···+(x**n)/n!+···

pluging into Taylor series we find:
    e**x= e**xi +e**xi * h + (e**xi *h**2)/2! + (e**xi* h**3)/3! + ... + (f'n'(xi)*h**n)/n! + R

    e**0= e**0 +e**0 * h + (e**0 h**2)/2! + (e**0 *h**3)/3! + ... + (f'n'(xi)*h**n)/n! + R

    1 = 1 + 1* h + (1 * h**2)/2! + (1 *h**3)/3! + ... + ((1)h**n)/n! + R
 sub in for h =x 
    1 = 1 + 1* x + (1 * x**2)/2! + (1 *x**3)/3! + ... + ((1)x**n)/n! + R
 which is the SAME as the Maclaurin
    1 = 1 +    x +     (x**2)/2! +    (x**3)/3!   + ···    (x**n)/n!+···


 
 (ii) Use a Taylor series to estimate f(x) = e**(−x) at   xi+1 = 2   for xi = 1.5. 
   Employ the zero-,
               first-, 
               second-, 
               and third-order
        versions and compute |εt| for each case.


        h= x[i+1]-xi = L = 2 - 1.5

f(xi )= f(xi)+f'(xi)h + (f''(xi)h**2)/2! + (f'3'(xi)h**3)/3! 
e**(−x)= e**(−x)
e**(−x)= e**(−x)-e**(−x).5  
e**(−x)= e**(−x)-e**(−x).5 + (e**(−x)*.5**2)/2! 
e**(−x)= e**(−x)-e**(−x).5 + (e**(−x)*.5**2)/2! - (e**(−x)*.5**3)/3! 

'''





'''

 3.b) Use zero- through third-order Taylor series expansions to predict f(1) for
 
 f(x) = 20*x**3−5*x**2 + 7*x − 80
 
 using a base point at xi=−1.  
 
 Compute the true percent relative error εt for each approxima-tion.



h = 2 = x[i+1] - xi = 1- -1

'''






if __name__ == '__main__':
    
    # test to see if the Rock code works
    x_max = 100
    skipBy = 1

    # set up empty lists
    x_list = [None] * (x_max)
    y_list = [None] * (x_max)
    for i in range(0,len(x_list)):
        
        x_list[i] = i*skipBy
        # run the height given a time: i
        y_list[i] = height(x_list[i])

    try:
        plt.scatter(x_list, y_list, s=15, edgecolors='none', c='blue')
        plt.show()
        
    except Exception as identifier:
        print("failed to show the matplotlib object:")
        print(identifier)
        exit(-1)
    print(" Finished with part 2")