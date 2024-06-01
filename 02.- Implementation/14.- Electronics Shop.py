"""
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.

Function Description

Complete the getMoneySpent function in the editor below.

getMoneySpent has the following parameter(s):

    int keyboards[n]: the keyboard prices
    int drives[m]: the drive prices
    int b: the budget

Returns

    int: the maximum that can be spent, or  -1 if it is not possible to buy both items

Solution:
"""
import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    coins, max_coins = 0, 0
    for i in range(len(keyboards)):
        coins = keyboards[i]
        for j in range(len(drives)):
            if keyboards[i] + drives[j] <= b:
                coins = keyboards[i] + drives[j]
                if coins > max_coins:
                    max_coins = coins
    return -1 if max_coins == 0 else max_coins

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
