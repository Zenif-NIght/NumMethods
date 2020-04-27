def Bisect(function,xLower, xUpper, Ead, n):
    # Bisection method to finds a root of a funtion.
    # xLower: lower bound guess.
    # xUpper: upper bound guess.
    # es: error threshold.
    # imax: max iterations threshold.
    iter =0
    xr = xLower
    ea = Ead
    xr_old = xr

    if (function(xLower) * function(xUpper) >= 0): 
        if function(xLower) == 0:
            return (xLower)
        elif function(xUpper) == 0:
            return (xUpper)
        
        print("You piced the Worng Vales xLower:"+str(xLower)+" and xUpper:"+str(xUpper)+"\n") 
        temp = xLower
        xLower = xUpper
        xUpper = temp
        
        return


    while (ea >= Ead) and (iter < n):
        xr_old = xr_old
        
        # this is the only change is you want to do the false position method 
        #  change xr = () 
        xr = (xLower + xUpper)/2 # bisection method
        print("Iteration:",iter," xr: ",xr)
        iter +=1
        if xr != 0 :
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
    print("x: "+str(x)+ " is the root approx Bisection method")
    return x


