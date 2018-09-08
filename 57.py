n,k=map(int,raw_input().split())
list=[int(s) for s in raw_input().split()]
if k in list:
    count=list.count(k)
    print count
else:
    print 0
    

  
