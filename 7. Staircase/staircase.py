#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for x in range(n, 0, -1):
        for y in range (1, n+1):
            if y < x:
                print(" ", end="")
            else:
                print("#", end="")
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)
