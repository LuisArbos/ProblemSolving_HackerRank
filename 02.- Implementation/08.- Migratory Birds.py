"""
Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

Function Description

Complete the migratoryBirds function in the editor below.

migratoryBirds has the following parameter(s):

    int arr[n]: the types of birds sighted

Returns

    int: the lowest type id of the most frequently sighted birds

Solution:
"""
import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    birds = {}
    for item in arr:
        if item in birds.keys():
            birds[item] += 1
        else:
            birds[item] = 1
    max_count = max(birds.values())
    keys = [key for key, count in birds.items() if count == max_count]
    return(min(keys))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
