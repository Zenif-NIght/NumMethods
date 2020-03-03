import math
#  goldenSearch
def goldenSearch(function,xl, xu,tol):

    goldenRatio = 2/(math.sqrt(5) + 1)

    # Use the goldon ratio to set initial points
    x1 = xu - goldenRatio * (xu - xl)
    x2 = xl + goldenRatio * (xu - xl)

    f1 = function(x1)
    f2 = function(x2)

    iter = 0
    deltaX = abs(xu - xl)
    Ead = tol
    numIteration = int(math.log2(deltaX/Ead))

    # while (abs(xu - xl) > tol):
    while( iter <= numIteration):
        iter = iter + 1

        if (f2 > f1):

            xu = x2
            print('New Upper Bound =', xu)
            print('New Lower Bound =', xl)
            # Set the new upper test point
            # Use result of the goldon ratio
            x2 = x1
            print('New Upper Test Point = ', x2)
            f2 = f1

            # Set the new lower test point
            x1 = xu - goldenRatio*(xu - xl)
            print('New Lower Test Point = ', x1)
            f1 = function(x1)
        else :
            print('f2 < f1')

            xl = x1
            print('New Upper Bound =', xu)
            print('New Lower Bound =', xl)

            # Set the new lower test point
            x1 = x2
            print('New Lower Test Point = ', x1)

            f1 = f2

            # Set the new upper test point
            x2 = xl + goldenRatio*(xu - xl)
            print('New Upper Test Point = ', x2)
            f2 = function(x2)

    print('Final Lower Bound =', xl)
    print('Final Upper Bound =', xu)
    finalPoint = (xl + xu)/2
    print('Final Local Minima =', finalPoint )
    return finalPoint
