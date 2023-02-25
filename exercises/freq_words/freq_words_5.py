import re
from collections import Counter
s=input("enter s: ")
s = s.strip('.')
a = list(re.split('[. \n]',s))
a.remove('')
a = Counter(a)
for k,v in a.items():
    print(k,v)    
