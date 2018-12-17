import sys,string,math
n=int(raw_input())
L=[int(x) for x in raw_input().split()]
a,b=max(L),min(L)
k=abs(L.index(a)-L.index(b))
print k
