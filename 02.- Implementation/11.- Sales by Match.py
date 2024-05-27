"""
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

    int n: the number of socks in the pile
    int ar[n]: the colors of each sock

Returns

    int: the number of pairs


Solution:
"""
import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pair_dict = {}
    total_pairs = 0
    for i in range(len(ar)):
        if ar[i] in pair_dict.keys():
            pair_dict[ar[i]] += 1
        else:
            pair_dict[ar[i]] = 1
    print(pair_dict)
    for key, count in pair_dict.items():
        if count >= 2:
            total_pairs += int(count / 2)
    return total_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
