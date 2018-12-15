n=int(raw_input())
L1=[int(x) for x in raw_input().split()]
L2=[int(x) for x in raw_input().split()]
if L1==L2[::-1]:
    print "yes"
else:
    print"no"
