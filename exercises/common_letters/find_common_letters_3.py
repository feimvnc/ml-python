s1=input('enter first string: ')
s2=input('enter second string: ')
l=[]

for ch in s1:
    if ch not in s2:
        pass 
    else:
        l.append(ch)

s3='.'.join(l)
print('{} - {} - {}'.format(s1, s2, s3))
