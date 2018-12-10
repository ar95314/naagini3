n=raw_input()
k=n.count(n[0])
for i in range(1,len(n)):
    if n.count(n[i])!= k:
        print "No"
        break
else : 
    print"Yes"
