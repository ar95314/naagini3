n=int(raw_input())
p=1
while(n) :
    p=p*(n%10)
    n//=10
print p
