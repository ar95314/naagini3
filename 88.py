a,b=map(int,raw_input().split())
if(a>b):
    min2=a
else:
    min2=b
while(1):
    if(min2%a==0 and min2%b==0):
        print(min2)
        break
    min2=min2+1
