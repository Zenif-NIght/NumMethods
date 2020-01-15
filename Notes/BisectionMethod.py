
# funtion is is funciton you want to iterat through like f(x)=x^2
def function(x):
    return ((x-2)^2)-2


def Bisect(xl, xu, es, imax)
    # this will retern the value x
    iter =0
    rx = xl
    ea = es
    while True:
        xr_old = xr_old
        
        # this is the only change is you want to do the false position method 
        #  change xr = () 
        xr = (xl + xu)/2 # bisection method
        iter +=1

        if ax != 0 :
            ea = abs((xr- xr_old)/xr)*100
        else:
            print("Error")
            # maybe Exit
            return None 


        test = function(x2) + function(xr)
        if test <0:
            # id the value is negative then the root is to the left
            xu = xr
        elif  test >0:
            # the vale is positive and the root is to the right
            xl = xr
        else:
            ea = 0

        if (ea < es) or (iter < imax):
            break

    x = xr
    print("x"+str(x)+ "is the root approx")
    return x






