#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    num_of_jumps = 0
    i = 0
    
    while True:
        if i <= len(c)-3:
            next_cloud = c[i+1]
            next2_cloud = c[i+2]
            
            if next_cloud == 0:
                if next2_cloud == 0:
                    i += 2
                    num_of_jumps += 1
                else:
                    i += 1
                    num_of_jumps += 1
            else:
                if next2_cloud == 0:
                    i += 2
                    num_of_jumps += 1
        
        elif i == len(c)-2:
            next_cloud = c[i+1]
            
            if next_cloud == 0:
                i += 1
                num_of_jumps += 1
            else:
                i += 1
        else:
            break

        print(i, end=" ")

    return num_of_jumps




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
