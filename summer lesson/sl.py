#!/bin/python3

import os
import sys


#
# Complete the howManyStudents function below.
#
def howManyStudents(m, c):
    # Return an array denoting the number of students taking each class.
    l=[0 for i in range(m)]
    for i in range (len(c)):
        l[c[i]]=l[c[i]]+1
    return l;

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = howManyStudents(m, c)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
