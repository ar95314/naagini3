x=raw_input()
f="".join([c[1]+c[0]for c in zip (x[::2],x[1::2])])
print f
