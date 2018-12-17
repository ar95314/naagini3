import sys
n=int(raw_input())
L=[int(x) for x in raw_input().split()]
dic1={}
for x in L :
    dic1[x]=dic1.get(x,0)+1
min1=sys.maxsize
for k,v in dic1.items():
    if v<min1:
        min=v
        key=k
print key
