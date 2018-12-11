a,b,c=map(int,raw_input().split())
if(a+b<=c or b+c<=a or c+a<=b):
    print "no"
else:
    print "yes"
