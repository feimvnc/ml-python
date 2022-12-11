# dictionary: key-value pairs, unordered, mutable

d = {"name": "john", "age": 42, "city":"New York"}
print(d)

# use dict function 
d2 = dict(name="alice", age=30, city="Boston")
print(d2)

# access with key 
v = d["name"]
print(v)

# raise exception if key not exist, KeyError: 'lastname'
# v2 = d["lastname"]
# print(v2)

# add key 
d["email"] = "email@example.com"
print(d)
 
# delete using del statement
del d["name"]
print(d) 

# delete using pop method 
d.pop("age")
print(d)

# remove last item when python >3.7, before arbitrary pair
d.popitem()
print(d)

# 2 common ways to check if key is in dict 
# use if statement 
if "name" in d2:
    print(d2["name"])

# use try 
try: 
    print(d2["name"])
except:
    print("error")

# loop through dict 
for key in d2: 
    print(key)

# loop through dict 
for value in d2.values(): 
    print(value)

# print both key and values 
for key, value in d2.items():
    print(key, value)

# copy 
d2_copy = d2    # now both assign to same memory, be careful
print(d2_copy)

# change dict copy also update original dict 
d2_copy["email"] = "example@example.com"
print(d2_copy)
print(d2)

# have an actual copy, use copy()
# original copy will not change 
d2_copy_actual = d2.copy()
# or 
d2_copy_actual2 = dict(d2)

# merge 2 dict , same key will be overwritten
d.update(d2)
print(d)

# key type can be string, number, tuples 
# but when using number as key, must use key value but not index 
d4 = {1:11, 2:22, 3:33}
print(d4)
# v = d4[0]   # this throws error 
v = d4[1]   # this works 

# use tuples as key 
t = (1,2)
# t = [1,2]  # list is not allowed, list is mutable, can't have same hash key 
d5 = {t: 3}     # tuple : sum 
print(d5)



