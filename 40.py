x=int(raw_input())
n1=1
n2=1
i=2
if x<=0:
    print("positive")
elif x==1:
    print a1,
else:
    print n1,
    print n2,
    while i<x:
        n3=n1+n2
        print n3,
        n1=n2
        n2=n3
        i=i+1
