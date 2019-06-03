#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    answer = []
    positives = 0
    negatives = 0
    zeroes = 0
    for elt in arr:
        if elt > 0: 
            positives += 1
        if elt < 0:
            negatives += 1
        if elt == 0:
            zeroes += 1
    positives = positives / len(arr)
    negatives = negatives / len(arr)
    zeroes = zeroes / len(arr)
    
    print(positives)
    print(negatives)
    print(zeroes)
    



    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
