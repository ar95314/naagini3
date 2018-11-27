m=int(raw_input())
rev=0
while(m>0):
    rem=m%10
    rev=(rev*10)+rem
    m=m/10
print rev
