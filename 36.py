import re
x = raw_input()
new = re.sub('[\w]+' ,'',x)
print (len(new))
