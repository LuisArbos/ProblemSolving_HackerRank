"""
A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivalTime >0).

Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled. 

Function Description

Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.

angryProfessor has the following parameter(s):
    int k: the threshold number of students
    int a[n]: the arrival times of the n students

Returns
    string: either YES or NO

Solution:
"""
import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    # Write your code here
    a_sorted = sorted(a)
    counter = 0
    for item in a_sorted:
        if item <= 0:
            counter += 1
    return "YES" if counter < k else "NO"
    #print(counter)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
