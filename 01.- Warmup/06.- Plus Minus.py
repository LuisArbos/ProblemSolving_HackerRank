"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

Example

arr = [1,1,0,-1,-1]

There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000. Results are printed as:

0.400000
0.400000
0.200000

Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

    int arr[n]: an array of integers

Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6 digits after the decimal. The function should not return a value. 

Solution:
"""

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos, neg, zero = 0, 0, 0
    for item in arr:
        if item == 0:
            zero+=1
        elif item > 0:
            pos += 1
        else:
            neg += 1
    zero = float(zero/len(arr))
    pos = float(pos/len(arr))
    neg = float(neg/len(arr))
    print(f'{pos:.5f}')
    print(f'{neg:.5f}')
    print(f'{zero:.5f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

