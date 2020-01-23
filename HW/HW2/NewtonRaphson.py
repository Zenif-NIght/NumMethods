def newtRap(function,derivitve, XGuess, es, imax):
    # XGuess: bound guess.
    # es: error threshold.
    # imax: max iterations threshold.

    iter =0
    xr = XGuess

    if function(XGuess) == 0:
        return (XGuess)

    while (iter < imax):
        h = function(xr) / derivitve(xr) 
        iter +=1
        xr = xr -h 
        # if abs(h)>= es:
        #     break
    x = xr
    print("x: "+str(x)+ " is the root approx using Newton Raphson method. ")
    return x
