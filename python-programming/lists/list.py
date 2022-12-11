# list is ordered mutable, allows duplicate elements 

from math import log2


print("hello")
l1 = ["a", "b", "c"]
print(l1)

l2 = [5, True, "a", "b"]
print(l2)

print(l2[0])  # list index starts 0 
print(l2[-2])

for x in l2:
    print(x)

if "b" in l2:
    print("yes")
else: 
    print("no")

print(len(l2))

l2.append("x")
print(l2)

l2.insert(1, "y")
print(l2)

p = l2.pop()
print(l2)

l2.remove("b")
print(l2)

l3 = l2.reverse()
print(l2)

l5 = [7,2,3,6]
l4 = sorted(l5)
print(l4)

# l2.clear() # remove all elements 
# print(l2)

l6 = [1]*5
print(l6)

print(l6 + l6)

print(l6[2:])

print(l6[::-1]) ##reverse list 

# list copy refer same memory data 
l7 = ["m", "n", "p"]
l77 = l7 
l77 = l7.copy 
l77 = list(l7)
l77 = l7[:]
l77.append("q")
print(l7)
print(l77)      # both has "q"

# list comprehension, create list in one line 
c = [1,2,3,4,5]
cc = [i*i for i in c]   # expression, for loop over list
print(c)
print(cc)

