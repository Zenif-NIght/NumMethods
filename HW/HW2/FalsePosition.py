def FalsePos(function,xLower, xUpper, es, imax):
    # False Position method to find a root of a funtion.
    # xLower:lower bound guess.
    # xUpper:upper bound guess.
    # es: error threshold.
    # imax: max iterations threshold.

    iter =0
    xr = xLower
    ea = es
    xr_old = xr

    if (function(xLower) * function(xUpper) >= 0): 
        if function(xLower) == 0:
            return (xLower)
        elif function(xUpper) == 0:
            return (xUpper)
        
        print("You picked the Wrong Values xLower:f("+str(xLower)+") = "+ str(function(xLower))+" and xUpper: f("+str(xUpper)+") = "+ str(function(xUpper))+"\n") 
        # return
        # print("You have not assumed right xLower:"+str(xLower)+" and left xUpper:"+str(xUpper)+"\n") 
        # xr = xUpper
        # xUpper = xLower
        # xLower = xr


    while (ea >= es) and (iter < imax):
        xr_old = xr
        # (a * func(b) - b * func(a))/ (func(b) - func(a)) 
        xr = (xUpper*function(xLower) - xLower *function(xUpper))/ (function(xLower)-function(xUpper))
        # xr = (xUpper*function(xLower)-xLower)/ (function(xLower)-function(xUpper))

        iter +=1
        if function(xr) == 0:
            return xr
        elif xr != 0 :
            ea = abs((xr- xr_old)/xr)*100
        else:
            print("Error")
            # maybe Exit
            return None 


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
    print("x: "+str(x)+ " is the root approx using False Position method. ")
    return x
