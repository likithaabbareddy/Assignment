# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 16:48:57 2017

@author: likitha
solution:
1. Take the values from the user.
2. The numbers are passed as arguments to a recursive function to find the power of the number.
3. If the exponential power is equal to 1, return the number itself.
4. If the power is not equal to 1, return the number multiplied with the power function that is called recursively with the arguments as the base and power minus 1.
5. Print the final result.
6. Exit.
"""

def power(x,n):
    if(n==1):
        return(x)
    if(n!=1):
        return(x*power(x,n-1))
x=int(input("Enter base value: "))
n=int(input("Enter exponential value: "))
print("Result:",power(x,n))