dict={1: 'one', 2:'two', 3:'three'}
l=[]
for i in dict.items():
    l.extend(list(i))

print(l)
