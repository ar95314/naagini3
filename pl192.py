import sys
n=int(raw_input())
L=[int(x) for x in raw_input().split()]
for x in range(1,n) :
    if x%2 == 1 :
        if L[x] <= L[x-1] :
            print('no')
            sys.exit()
    else :
        if L[x] >= L[x-1] :
            print('no')
            sys.exit()
print('yes')
