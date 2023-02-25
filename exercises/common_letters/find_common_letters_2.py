s1=input("enter first string: ")
s2=input("enter second string: ")
s1=set(list(s1))
s2=set(list(s2))
common=list(s1.intersection(s2))
print(common)

