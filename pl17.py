l,r=map(int,raw_input().split())
for i in range(max(l,r),l*r+1) :
    if (i%l == 0) and (i%r == 0) :
        ans=i
        break
print ans
