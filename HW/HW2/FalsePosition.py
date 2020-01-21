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

    if (function(xl) * function(xu) >= 0): 
        print("You have not assumed right xl:"+str(xl)+" and xu:"+str(xl)+"\n") 
        return


    while (ea >= es) and (iter < imax):
        xr_old = xr
        
        xr = xu-(function(xu))/ (function(xl)-function(xu))

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

    # iter = 0;						%iteration count
    # xr = xl;						%real root
    # ea = es; 						%error
    # %while the error is above a threshold, or iterations below a threshold
    # while ea>=es && iter<imax 
    #     xrold = xr;					%keep track of previous root
    #     %false position formula
    #     xr = xu-((0.8*xu.^5 - 8*xu.^4 + 46*xu.^3 - 90*xu.^2 +83*xu - 26)*(xl-xu))/...
    #         ((0.8*xl.^5 - 8*xl.^4 + 46*xl.^3 - 90*xl.^2 +83*xl - 26)-...
    #         (0.8*xu.^5 - 8*xu.^4 + 46*xu.^3 - 90*xu.^2 +83*xu - 26));
    #     iter = iter+1;				%increment iteration count
    #     if xr~=0 					%if root is not zero
    #         ea = abs((xr-xrold)/xr)*100; 	%avoid dividing by zero
    #     end
    #     test = (0.8*xl.^5 - 8*xl.^4 + 46*xl.^3 - 90*xl.^2 +83*xl - 26)*...
    #         (0.8*xr.^5 - 8*xr.^4 + 46*xr.^3 - 90*xr.^2 +83*xr - 26);
    #     if test<0					%if product is negative
    #         xu=xr;					%upper bound is new root
    #     elseif test>0				%if product is positive
    #         xl=xr;					%lower bound is new root
    #     else
    #         ea = 0;					%error is zero if product is zero
    #     end
    # end
    # x=xr;
