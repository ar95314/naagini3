# your code goes here
import re
a = raw_input()
new = re.sub('[\w]+' ,'',a)
print (len(new))
