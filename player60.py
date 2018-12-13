s1,s2=raw_input().split()
for c in s1:
    if c in s2:
        print "yes"
        break
else:
    print "no"
