#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zero += 1
    
    print("{0:.4f}".format(positive/len(arr)))
    print("{0:.4f}".format(negative/len(arr)))
    print("{0:.4f}".format(zero/len(arr)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
