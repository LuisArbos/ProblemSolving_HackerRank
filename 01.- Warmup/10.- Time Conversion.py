"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s='12:01:00PM'

Return '12:01:00'.

s='12:01:00AM'

Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

    string s: a time in 12 hour format

Returns

    string: the time in 24 hour format

Input Format

A single string s that represents a time in -hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM ).

Solution:
"""
import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hours = s[:2]
    rest = s[2:8]
    time_format = s[8:]
    result = ""
    if time_format == "AM":
        if hours == "12":
            result = "00"+rest
        else:
            result = hours + rest
    elif time_format == "PM":
        if hours != "12":
            hours = str(int(hours) + 12)
            #hours += 12 
            result = hours + rest 
        else:
            result = hours + rest
    #result = hours + rest + time_format
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

