def main():
	c=1
	m=int(input())
	for i in range(1,m):
		c=c*i
	print(c)
try:
	main()
except:
	print('invalid')
