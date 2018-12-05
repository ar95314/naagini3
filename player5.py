input=raw_input()
st=list(input)
b=[]
for x in st:
	if x=="V" or x=="v":
		b.append(5)
	elif x=="I" or x=='i':
		b.append(1)
	elif x=="X" or x=='x':
		b.append(10)
	elif x=="L" or x=='l':
		b.append(50)
	elif x=="C" or x=='c':
		b.append(100)
	elif x=="D" or x=='d':
		b.append(500)
	elif x=="M" or x=='m':
		b.append(1000)
 
k=b.index(max(b))
ans=max(b)
if k==0:
	for x in range(1,len(b)):
		ans=ans+b[x]
else:
	for x in range(len(b)-1):
		ans=ans-b[x]
print(ans)
