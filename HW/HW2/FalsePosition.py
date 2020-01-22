def FalsePos(function,xl, xu, es, imax):
    # False Position method to find a root of a funtion.
    # xl:lower bound guess.
    # xu:upper bound guess.
    # es: error threshold.
    # imax: max iterations threshold.

    iter =0
    xr = xl
    ea = es
    xr_old = xr

    # if (function(xl) * function(xu) >= 0): 
    #     print("You have not assumed right xl:"+str(xl)+" and left xu:"+str(xu)+"\n") 
    #     # xr = xu
    #     # xu = xl
    #     # xl = xr


    while (ea >= es) and (iter < imax):
        xr_old = xr
        # (a * func(b) - b * func(a))/ (func(b) - func(a)) 
        xr = (xu*function(xl)-xl)/ (function(xl)-function(xu))

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
    print("x: "+str(x)+ " is the root approx using False Position method. ")
    return x
