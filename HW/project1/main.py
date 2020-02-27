
'''
1. Linear algebraic equations can arise in the solution 
    of differential equations. For example, the following heat 
    equation describes the equilibrium temperature 
    T = T(x)(oC) 
    at a point x (in meters m) along a long thin rod,

    d2T/dx2 = h′(T − Ta), (1) 

    where Ta = 10oC denotes the temperature of the surrounding 
    air, and h′ = 0.03 (m−2) is a heat transfer coefficient. Assume 
    that the rod is 10 meters long (i.e. 0 ≤ x ≤ 10) and has 
    boundary conditions imposed at its ends given by T(0) = 20oC 
    and T(10) = 100oC.
'''


'''
a) Using standard ODE methods, which you do not need to repeat here,
    the general form of an analytic solution to (1) can be derived as

    T(x)=A+Beλx +Ce−λx, (2)

    where A, B, C, and λ are constants. Plug the solution of type (2) 
    into both sides of equation (1). This should give you an equation 
    that must be satisfied for all values of x, for 0 ≤ x ≤ 10, for some 
    fixed constants A, B, C, and λ. Analyze this conclusion to determine 
    what the values of A and λ must be.
'''

'''
(b) Next, impose the boundary conditions T (0) = 20 oC and
    T (10) = 100 oC to derive a system of 2 linear algebraic equations 
    for B and C. Provide the system of two equations you have derived.
'''
'''
(c) Use one of the numerical algorithms you developed for 
    homework 3 (Gauss elimination or LU decomposition) to solve the 
    algebraic system you de- rived in question 2(b) above, and obtain an 
    analytic solution to (1) of the form (2). By analytic solution we mean
    an explicit solution to equation (1) which is valid for each x in
    the interval [0, 10].
'''
'''
(d) Next we will discuss how to obtain a numerical solution to (1). 
    That is, we will seek to obtain an approximate solution to (1) which 
    describes the value of T at 9 intermediate points inside the interval 
    [0,10]. More precisely, the equation (1) can be transformed into a 
    linear algebraic system for the temperature at 9 interior points 
T1 = T(1),
 T2 = T(2), 
 T3 = T(3), 
 T4 =T(4),
 T5 =T(5),
 T6 =T(6),
 T7 =T(7),
 T8 =T(8),
 T9 =T(9),
    by
    using the following finite difference approximation for the second 
    derivative at the ith interior point,

d2Ti = Ti+1 −2Ti +Ti−1, (3) dx2 (∆x)2
    where
1≤i≤9,
T0 =T(0)=20oC,
T10=T(10)=100oC,
    and ∆x is the equal spacing between consecutive interior points 
    (i.e. with 9 equally spaced interior points inside [0,10] it holds 
    that ∆x = 1). Use (3) to rewrite (1) as a system of 9 linear algebraic
    equations for the unknowns T1, T2, T3, T4, T5, T6, T7, T8, and T9. 
    Provide the system of 9 equations you have derived.
'''


'''
(e) Use one of the numerical algorithms you developed for homework 3 
    (Gauss elimination or LU decomposition) to solve the system derived 
    in question 1(d) above. Validate your numerical solution by comparison 
    to the analytic solution that you obtained in 1(c) through depicting 
    the two solutions on plots over the interval 0 ≤ x ≤ 10.
'''

'''
(f) Write a function that takes as input the number of interior nodes
    n desired for your numerical solution (i.e. n = 9 in 1(d) above),
    and outputs the numerical solution to (1) in the form of the interior 
    node values T1 = T(∆x), T2 = T(2∆x),..., Tn = T(n∆x).
'''
'''
(g) Produce and submit 4 plots that compare your analytic solution 
    to (1) derived in question 2(b) to the numerical solution generated 
    in question 2(f) for n = 1, n = 4, n = 9, and n = 19, respectively.
'''

'''
2. Develop an algorithm that uses the golden section search to locate 
    the minimum of a given function. Rather than using the iterative
    stopping criteria we have previously implemented, design the 
    algorithm to begin by determining the number of iterations n required 
    to achieve a desired absolute error |Ea| (not a percentage), where 
    the value for |Ea| is input by the user. You may gain insight by 
    comparing this approach to a discussion regarding the bisection 
    method on page 132 of the textbook. Test your algorithm by applying
    it to find the minimum of f(x) = 2x+ 6 with initial guesses xl = 1 
    and xu = 5 and x desired absolute error |Ea| = 0.00001.
'''

'''
3. Given f(x,y)=2xy+2y−1.5x2−2y2,
(a) Start with an initial guess of (x0,y0) = (1,1) and determine 
    (by hand is fine) two iterations of the steepest ascent method to 
    maximize f(x,y).

(b) What point is the steepest ascent method converging 
    towards? Justify your answer without computing any more 
    iterations.
'''