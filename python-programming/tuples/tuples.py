# tuples ordered, immutable, allows duplicate elements 
# different from list, can't be changed after creation 
# can be efficient becuase immutable 

t = ("a", "b", "c") # create 
t1 = "a", "b", "c"
print(t)
print(t1)

t2 = "a"    # treat as string 
print(type(t2))     #class string

t3 = "a",   # put comma at end, treat as tuples
print(type(t3)) # class tuple 

t4 = tuple(["a", 1, "b"])
print(t4)

i = t4[2]
print(i)

# i[0] = "x"    # not allowed, tuples is immutable 

for i in t4:
    print(i)

if "a" in t4: 
    print("yes")
else: 
    print("no")

print(len(t4))
print(t4.count('b'))
print(t4.index("a"))

# convert to list 
l = list(t4)
print(l) # ['a', 1, 'b']

# convert to tuples 
t5 = tuple(l)
print(t5)   #('a', 1, 'b')

t6 = (1,2,3,4,5,6)
b = t6[2:5]
#b = t6[::2] # every 2nd element 
print(b)    #(3, 4, 5)

t7 = "a", 2, "b"
v1, v2, v3 = t7     # unpack tuples 
print(v1)
print(v2)
print(v3)

import sys 
my_list = [0, 1, 2, 3]
my_tuple = (0, 1, 2, 3) 
print(sys.getsizeof(my_list), "bytes")  # 120 bytes
print(sys.getsizeof(my_tuple), "bytes") # 72 bytes, even same elements 

import timeit 
print(timeit.timeit(stmt="[1,2,3,4,5]", number=100)) #8.23
print(timeit.timeit(stmt="(1,2,3,4,5)", number=100)) # 1.43 , tuples is efficient