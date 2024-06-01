"""
The factorial of the integer n, written n!, is defined as:

n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

Calculate and print the factorial of a given integer. 

Input Format

Input consists of a single integer n

Solution:
"""
import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    print(math.factorial(n))        

if __name__ == '__main__':
    n = int(input().strip())
    extraLongFactorials(n)
