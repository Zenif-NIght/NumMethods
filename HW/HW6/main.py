import math
import numpy as np
import matplotlib.pyplot as plt
import prob1 as p1

def funct_temp_1A(x,y):
    return x**2 - 3*y**2 + x*y + 72

if __name__ == "__main__":
    print("Starting Application: ") 
    p1.pob1a(-2,2,0,4,6,funct_temp_1A)