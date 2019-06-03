#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.

def diagonalDifference(arr):
    first =0
    second=0
    i=0
    for count in range(len(arr[0])):
        first += arr[count][count]
        second += arr[count][(len(arr[0])-count-1)]
    return abs(first-second)
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
