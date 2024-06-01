"""
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after n growth cycles?

Function Description

Complete the utopianTree function in the editor below.

utopianTree has the following parameter(s):
    int n: the number of growth cycles to simulate

Returns
    int: the height of the tree after the given number of cycles

Solution:
"""
import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    total = 1
    if n != 0:
        for i in range(1, n+1):
            print("i -> ", i)
            if i % 2 != 0:
                total *= 2
            else:
                total += 1
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
