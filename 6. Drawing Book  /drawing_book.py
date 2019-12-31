#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    front_count = p//2

    if n%2 == 0 and p%2 != 0:
        back_count = (n-p)//2+1
    else:
        back_count = (n-p)//2

    # return "A: " + str(front_count)+ "\nB: " + str(back_count)

    if front_count < back_count:
        return front_count
        # return "A: " + str(front_count)
    else:
        return back_count
        # return "B: " + str(back_count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

