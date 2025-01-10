#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    d1=0
    d2=0
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                d1+=arr[i][j]
                # print(d1)
            if (i == n - j -1):
                d2+= arr[i][j]
                # print(d2)
    return abs(d1-d2)



if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)
    print(result)
