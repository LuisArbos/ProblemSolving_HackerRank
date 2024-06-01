"""
A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. The character must jump from cloud to cloud until it reaches the start again.

There is an array of clouds, c and an energy level e=100. The character starts from c[0] and uses 1 unit of energy to make a jump of size k to cloud c[(i+k)%n]. If it lands on a thundercloud, c[i]=1 , its energy (e) decreases by 2 additional units. The game ends when the character lands back on cloud 0.

Given the values of n, k, and the configuration of the clouds as an array c, determine the final value of after the game ends.

Function Description

Complete the jumpingOnClouds function in the editor below.
jumpingOnClouds has the following parameter(s):
    int c[n]: the cloud types along the path
    int k: the length of one jump

Returns
    int: the energy level remaining.

Solution:
"""
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    index = 0
    while energy>0:
        index = (index + k) % n
        energy -= 1
        if c[index] == 1:
            energy -= 2
        if index == 0:
            return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
