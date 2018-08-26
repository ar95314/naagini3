year=int(input("enter the year number:"))
if(year%4==0):
    print("%d is a leaf year" %year)
elif (year%400==0):
    print("%d is a leaf year" %year)
else:
    print("%d is not a leaf year" %year)
    
