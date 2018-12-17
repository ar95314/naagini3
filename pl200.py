c=str(raw_input())
print(''.join([y for x,y in enumerate(c) if y not in c[:x]]))
