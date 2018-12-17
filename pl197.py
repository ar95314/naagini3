import sys,string,math
n=int(raw_input())
L=[int(x) for x in raw_input().split()]
value=abs(max(L)-min(L))
print value
