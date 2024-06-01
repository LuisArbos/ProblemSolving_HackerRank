"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

    The player with the highest score is ranked number 1 on the leaderboard.
    Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

Function Description

Complete the climbingLeaderboard function in the editor below.

climbingLeaderboard has the following parameter(s):
    int ranked[n]: the leaderboard scores
    int player[m]: the player's scores

Returns
    int[m]: the player's rank after each new score


Solution:
"""
import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    unique_ranked = sorted(set(ranked), reverse=True)
    
    result = []
    for point in player:
        while unique_ranked and point >= unique_ranked[-1]:
            unique_ranked.pop()
        result.append(len(unique_ranked) + 1)
    
    return result
        
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
