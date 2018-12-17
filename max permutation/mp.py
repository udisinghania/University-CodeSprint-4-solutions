#!/bin/python3

import os
import sys


# Complete the function below.

def maximumPermutation(w, s):
    # Return the string representing the answer.
    r=list(w)
    t=list(s)
    f=0
    for i in range (len(r)):
        if r.count(r[i])<=t.count(r[i]): 
            f=f+1
    if f!=len(r):
        return '-1';
    else:
        
        return w;


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_i in range(t):
        w = input()

        s = input()

        result = maximumPermutation(w, s)

        f.write(result + "\n")

    f.close()
