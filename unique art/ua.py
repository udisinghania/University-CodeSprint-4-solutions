#!/bin/python3

import os
import sys

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().rstrip().split()))
    q = int(input())
    if n>=1 and q>=1:
        l=[]
        h=[]
        for q_itr in range(q):
            ij = input().split()
            l.append(int(ij[0]))
            h.append(int(ij[1]))
        for i in range (len(l)):
            if l[i]>=1 and h[i]<=n and l[i]<=h[i]: 
                v=[]
                for j in range (l[i]-1,h[i]):
                    r=0
                    for y in range (l[i]-1,h[i]):
                        if t[j]==t[y] and j!=y:
                            r=r+1
                    if r<1:
                        v.append(t[j])
                print(len(v))
