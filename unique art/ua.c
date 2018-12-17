#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
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
*/
int main()
{
    long long int n,q;
    scanf("%lld",&n);
    long long int t[n],i,j,y;
    for (i=0; i<n; i++)
    {scanf("%lld",&t[i]);}
    scanf("%lld",&q);
    if (n>=1 && q>=1)
    {
     long long int l[q],h[q];
     for (i=0; i<q; i++)
    {scanf("%lld",&l[i]);
     scanf("%lld",&h[i]);}
     for (i=0; i<q; i++)
     {
         if (l[i]>=1 && h[i]<=n && l[i]<=h[i])
         {
             long long int v=0;
             for (j=l[i]-1; j<h[i]; j++)
             {
                 long long int r=0;
                 for (y=l[i]-1; y<h[i]; y++)
                 {
                     if (t[j]==t[y]&& j!=y)
                     {r=r+1;}
                 }
                 if (r<1)
                 {v=v+1;}
             }
             printf("%lld\n",v);
         }
     }
       
    }
    return 0;
}
