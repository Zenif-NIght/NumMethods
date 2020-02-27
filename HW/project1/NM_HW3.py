#  Authored by Christopher Allred
#  A02233404
#  Numerical Methods
#  Spring 2020
import numpy as np
import math

'''
Homework 3 is dueonlinethrough Canvas in PDF format by 11:59PM on Friday February 7.You are required to submit
 code for all functions and/or subroutines built to solvethese problems, which is designed to be easy to read 
 and understand, in your chosenprogramming language,and which you have written yourself.  The text fromyour 
 code should both be copied into a single PDF file submitted on canvas.Yoursubmitted PDF must also include 
 responses to any assigned questions,which for problems requiring programming should be based on outputfrom 
 your code.   For  example,  if  you  are  asked  to  find  numerical  answers  to  aproblem, the numbers
  should be included in your submission.
  
  1.  Given the equations
  10*x1+ 2*x2−x3= 27
  −3*x1−6*x2+ 2*x3=−61.5
  x1+x2+ 5x3=−21.5

  [ 10 2 -1 |27 
    -3]

  (a)  Solve using naive Gauss elimination (by hand).  Show all steps of the com-putation.

  
  (b)  Substitute your results into the original equations to check your answers.
  

  2.  Given the equations
  x1+ 2*x2−*x3= 2
  5*x1+ 2*x2+ 2*x3= 9
  −3*x1+ 5*x2−*x3= 1,
  (a)  Solve by Gauss elimination with partial pivoting using code you have written your self
  (see Figure 9.6 on page 268 of text for pseudocode - beware of typosand/or unneccessary components!).
'''
TOLERANCE = 0.0001

def substitute(a, b):
    n = len(a)
    aCopy = a[:]
    x = [None]*(n)
    # x[n] = b[n]/aCopy[n][n]
    for i in range(n-1,-1,-1):
        # sum = b[i]
        x[i] =aCopy[i][n]/aCopy[i][i]
        for j in range( i-1,-1,-1 ):
            # sum = sum + aCopy[i][j]*x[j]
            aCopy[j][n] -= aCopy[j][i] *x[i]
            
    return x



def guss2(a, b):
    print(np.matrix(a))
    print("Solution:...")
    n = len(a)-1
    m = len(a[1])-1
    er = 0

    # get the Max val in each row
    s = [None] * (n+1)
    for i in range(0,n+1):
        s[i] = abs(a[i][0])
        for j in range( 1,n+1):
            if abs(a[i][j]) > s[i]:
                s[i] = abs(a[i][j])
            
        
    
    #Elimination:
    for k in range(0,n+1):
        # print("k:" +str(k))
        #Pivot:
        p = k
        big = abs(a[k][k]/s[k])
        for ii in range(k+1,n+1):
            dummy = abs(a[ii][k]/s[ii])
            if dummy > big:
                big = dummy
                p = ii
            
        # Pivot
        if p != k:
            for jj in range( k,n+1):
                dummy = a[p][jj]
                a[p][jj] = a[k][jj]
                a[k][jj] = dummy
            
            dummy = b[p]
            b[p] = b[k]
            b[k] = dummy
            dummy = s[p]
            s[p] = s[k]
            s[k] = dummy
        

        if abs(a[k][k]/s[k]) < 0:
            er =- 1
            break #EXIT FOR
        
        for i in range(k+1,n+1):

            factor =- a[i][k]/a[k][k]
            for j in range (k,m+1):

                a[i][j] = a[i][j]+factor*a[k][j]

            b[i] = b[i]+factor*b[k]

    if abs(a[n][n]/s[n]) < 0:
        er = -1
    print(np.matrix(a))
    print("Coefficients: " + str(np.matrix(b)))
    # Elimination
    if er != -1:
        
        #Substitute:
        vals = substitute(a,b)
        print("Solution Values: "+ str(vals))
        return vals 
        






'''
  (b)  Substitute your results into the original equations to check your answers.


  3.  Given the equations

  8*x1+ 4*x2−*x3= 11
  −2*x1+ 5*x2+*x3= 4
  2*x1−*x2+ 6*x3= 7

  (a)  Solve using LU decomposition without pivoting (by hand).  Show all steps ofthe computation.
  (b)  Determine the matrix inverse using LU decomposition (by hand), and verifythat [A][A]−1= [I].4.  
  Given the equations
  2*x1−6*x2−x3=−38
  −3*x1−*x2+ 7*x3=−34
  −8*x1+x2−2*x3=−20,
  
  (a)  Solve  using  LU  decomposition  with  partial  pivoting  using  code  you  havewritten  yourself 
   (see  Figure  10.2  on  page  286  for  pseudocode  -  beware  oftypos and/or unnecessary components!).
   
   (b)  Determine the matrix inverse using code you have written yourself (see Fig-ure 10.5 on page 290 for 
   pseudocode - beware of typos and/or unnecessarycomponents!).
'''



if __name__ == "__main__":

    A1 =[[1,  1, 10],
        [math.exp(3) , math.exp(-3),  90]]

    bConsts1 = [10,90]

    guss2(A1,bConsts1)

