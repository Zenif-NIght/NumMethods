def Bisect(function,xl, xu, es, imax):
    # Bisection method to finds a root of a funtion.
    # xl: lower bound guess.
    # xu: upper bound guess.
    # es: error threshold.
    # imax: max iterations threshold.
    iter =0
    xr = xl
    ea = es
    xr_old = xr

    if (function(xl) * function(xu) >= 0): 
        print("You have not assumed right xl:"+str(xl)+" and xu:"+str(xl)+"\n") 
        return


    while (ea >= es) and (iter < imax):
        xr_old = xr_old
        
        # this is the only change is you want to do the false position method 
        #  change xr = () 
        xr = (xl + xu)/2 # bisection method
        iter +=1

        if xr != 0 :
            ea = abs((xr- xr_old)/xr)*100
        else:
            print("Error")
            # maybe Exit
            return None 


        test = function(xl) * function(xr)
        if test <0:
            # id the value is negative then the root is to the left
            xu = xr
        elif  test >0:
            # the vale is positive and the root is to the right
            xl = xr
        else:
            ea = 0

    x = xr
    print("x: "+str(x)+ "is the root approx")
    return x






