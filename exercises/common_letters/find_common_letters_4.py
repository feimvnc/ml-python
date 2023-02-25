s1=input('enter first string: ')
s2=input('enter second string: ')
t=[]
for s in s1:
    if s in s2:
        if s in t:
            continue
        else:
            t.append(s)
print(s1, s2, t)
