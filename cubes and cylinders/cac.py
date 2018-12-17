#!/bin/python3

import os
import sys


# Complete the function below.

def maximumPackages(S, K, R, C):
    # Return the maximum number of packages that can be put in the containers.
    p=sum(C)
    return p;        
        


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])#no. of types of package
    m = int(nm[1])#no. of cylindrical containers

    #S_size = int(input())

    S = list(map(int, input().rstrip().split()))#edge length of package 
    #K_size = int(input())

    K = list(map(int, input().rstrip().split()))#no. of copies of package type

    #R_size = int(input())

    R = list(map(int, input().rstrip().split()))#radius of cylinder

    #C_size = int(input())

    C = list(map(int, input().rstrip().split()))#capacity of cylinder

    result = maximumPackages(S, K, R, C)

    f.write(str(result) + "\n")

    f.close()
