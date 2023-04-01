# dictionaris in python, think it is a look-up table of key-value pairs
# or hash map, key value pairs, key is unique identifiers 
# ordered, changable, no dupliates 


# create empty dict , curly brackets 
dicta = {}
dictb = dict() 

# create 2 dicts, keys are commonly strings or numbers 
dicta = {"a": 1, "b": 2, "c":3}
dictb = dict({"a":1, "b":2, "c":3})
print(dicta, dictb)
# {'a': 1, 'b': 2, 'c': 3} {'a': 1, 'b': 2, 'c': 3}

# access key/value
print(dicta["c"])      # 3
# print(dicta["x"])      # KeyError: 'x', not found 

# update value 
dicta["a"] = 10
print(dicta["a"])       # 10
 
# iterate dict for all key/values
# items() returns a list resemble 2d list of tuples
# items = [(), (), ()]
for key, value in dicta.items():
    print(f"key: {key}, value: {value}")
# key: a, value: 10
# key: b, value: 2
# key: c, value: 3


print(f"get all keys: {dicta.keys()}")
# get all keys: dict_keys(['a', 'b', 'c'])

print(f"get all values: {dicta.values()}")
# get all values: dict_values([10, 2, 3])


# remove the last item {"c": 3}
dicta.popitem()
print(dicta)
# {'a': 10, 'b': 2}

# remove all items 
dictb.clear()
print(dictb)
# {}


# create a dict using for loop
a = ['a', 'b', 'c']
b = [1, 2, 3]
my_dict = {}
for (key, value) in zip(a, b):
    my_dict[key] = value 
print(my_dict)     # {'a': 1, 'b': 2, 'c': 3}

# create a dict using range 
a = ['a', 'b', 'c']
b = [1, 2, 3]
my_dict2 = {}
for i in range(len(a)):
    my_dict2[a[i]] = b[i]

print(my_dict2)     # {'a': 1, 'b': 2, 'c': 3}

# dict comprehension 
my_dict3 = {
    key: value for (key, value) in zip(a, b)
}
print(f"my_dict3: {my_dict3}")  # my_dict3: {'a': 1, 'b': 2, 'c': 3}

# replace dict key value using dict comprehension 

my_dict4 = my_dict3
my_dict4 = {
    (key+"_key" if key != 'a' else "x"):   # replace a with 'x', other keys add "_key"
    (val if val != 1 else 100)      # replace value of a 
    for (key, val) in my_dict4.items()  
}
print(f"my_dict4: {my_dict4}")    
# my_dict4 {'x': 1, 'b_key': 2, 'c_key': 3}
# my_dict4: {'x': 100, 'b_key': 2, 'c_key': 3}

# from list to dict 
# use dict comprehension to replace below for loop


import random 
bases = ["A", "T", "C", "G"]   # base list 
strand1 = random.choices(bases, k=10)   # 10 randoms items from list 
print(strand1 )

dna = {
    key:
    [val, ("T" if val=="A" else "A" if val == "T"
    else "C" if val == "G" else "G")] 
    for (key, val) in enumerate(strand1)
    }
print(dna)
# {0: ['G', 'C'], 1: ['A', 'T'], 2: ['T', 'A'], 3: ['A', 'T'], 4: ['T', 'A'], 5: ['C', 'G'], 6: ['C', 'G'], 7: ['A', 'T'], 8: ['A', 'T'], 9: ['C', 'G']}


# use dict comprehension to replace below for loop
# dna = {}
# for idx, b in enumerate(strand1):
#     if b == 'A': 
#         b2 = 'T'
#     elif b == 'T':
#         b2 = 'A'
#     elif b == 'C':
#         b2 = 'G'
#     else:
#         b2 = 'A'
#     dna[idx] = [b, b2]
# print(dna)
# {0: ['C', 'G'], 1: ['T', 'A'], 2: ['T', 'A'], 3: ['C', 'G'], 4: ['T', 'A'], 5: ['C', 'G'], 6: ['T', 'A'], 7: ['G', 'A'], 8: ['A', 'T'], 9: ['C', 'G']}


# create dict from 2 lists 
import random 
import string 

keys = ['id', 'username', 'password']
users = ["user1", "user2"]

data = [{
    key: (i if key == "id" 
    else users[i] if key == "username" 
    else "".join(random.choices(string.printable, k=8))) 
    for key in keys} 
    for i in range(len(users))
    ]

print(data)
[{'id': 0, 'username': 'user1', 'password': "H2G5q!T'"}, {'id': 1, 'username': 'user2', 'password': 'o|9UjlwZ'}]


# print(string.printable)
# use join to conver list to string 
# password = "".join(random.choices(string.printable, k=8))
# print(password)
