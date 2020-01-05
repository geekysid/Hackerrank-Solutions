# Enter your code here. Read input from STDIN. Print output to STDOUT

import os
import sys

def stringManipulator(n, p):
    string=""
    for i in range(n):
        string += p[i][::2] + " " + p[i][1::2] + "\n"
    
    # print(string)
    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = [input() for i in range(n)]

    result = stringManipulator(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()