def Secant(function,xLower, xUpper, es, imax):
    # Secant method to finds a root of a funtion.
    # xLower: lower bound guess.
    # xUpper: upper bound guess.
    # es: error threshold.
    # imax: max iterations threshold.
    iter =0
    xr = xLower
    ea = es
    xr_old = xr

    while (ea >= es) and (iter < imax):

        xr = xUpper - (function(xUpper)/
            (function(xUpper)-function(xLower))) * (xUpper - xLower) 
        xr_old = xr
        iter +=1

        test = function(xLower) * function(xr)
        if test <0:
            # id the value is negative then the root is to the left
            xUpper = xr
        elif  test >0:
            # the vale is positive and the root is to the right
            xLower = xr
        else:
            ea = 0

    x = xr
    print("x: "+str(x)+ " is the root approx Bisection method")
    return x



