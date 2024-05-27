"""
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

Function Description

Complete the breakingRecords function in the editor below.

breakingRecords has the following parameter(s):

    int scores[n]: points scored per game

Returns

    int[2]: An array with the numbers of times she broke her records. Index 0 is for breaking most points records, and index 1 is for breaking least points records. 

Solution:
"""
import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    minimum, maximum, count_min, count_max = 0, 0, 0, 0
    for i in range(len(scores)):
        if i == 0:
            minimum = scores[i]
            maximum = scores[i]
            count_min = 0
            count_max = 0
        else:
            if scores[i]<minimum:
                minimum = scores[i]
                count_min += 1
            elif scores[i]>maximum:
                maximum = scores[i]
                count_max += 1
    return count_max, count_min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
