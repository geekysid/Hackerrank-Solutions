#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sum_of_step = 0
    valley = 0
    i = 0;

    for step in s:
        i += 1
        if step == 'U':
            sum_of_step += 1
            if sum_of_step == 0:
                valley += 1
        elif step == 'D':
            sum_of_step -= 1 
    
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
