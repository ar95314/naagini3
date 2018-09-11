p=raw_input()
temp=p;
rev=0;
while(p>0):
    rem=p%10
    rev=rev*10+rem
    p=p//10
if(temp==rev):
    print("yes")
else:
    print("no")
 
