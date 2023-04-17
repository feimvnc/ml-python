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


# dictionaries used in modules, classes, instances, JSON, YAML, RelationalDB, multi-sets, sets, namespaces 
# dictionary, also is called associated arrays, abstract data structure 
# can be implemented using hash tables (aka hash maps)
# dict key must be hashable 

# hash values: used for hash tables (dictionaries), position index 
# key has to be hashable type 

# create dict using comprehension 
# pythonic way
d = {str(i): i**2 for i in range(1,5)}
print(d)
# {'1': 1, '2': 4, '3': 9, '4': 16}

# non-pythonic way 
d1 = {}
for i in range(1,5):
    d1[i] = i**2 
print(f"d1: {d1}")
# d1: {1: 1, 2: 4, 3: 9, 4: 16}

# but when things gets more complex, using look makes sense 
'''
d = {}
url = 'http://localhost/user/{id}'
for i in range(n):
    response = requests.get(url.format(id=i))
    user_json = response.json()
    user_age = int(use_json['age'])
    if user_age >= 18:
        user_name = user_json['fullName'].strip()    # dict value
        user_ssn = user_json['ssn]      # dict key 
        d[user_ssn] = user_name         # add to d 
'''

# create dict with fromkeys()
# d = dict.fromkeys(iterable, value)   # any iterable, all set to same value 
d2 = dict.fromkeys(['a', (0,0), 100], 'NA')
print(d2)
# {'a': 'NA', (0, 0): 'NA', 100: 'NA'}

d3 = dict.fromkeys((i**2 for i in range(1,5)), False)
print(d3)
# {1: False, 4: False, 9: False, 16: False}

# counters = dict.fromkeys(['a', 'b', 'c], 0)
# counters = dict.fromkeys('abc', 0)  # same as above 

keys = ['a', 'b', 'c']
values = (1,2,3)
d = {k: v for k,v in zip(keys, values)}

# above is the same as below 
d = {}
for k, v in zip(keys, values):
    d[k] = v


# create a dict with condition 
keys = 'abcd'
values = range(1,5)
d = {k: v for k, v in zip(keys, values) if v %2 == 0}


# create a dict using list comprehension
x_coords = [-2, -1, 0, 1, 2]
y_coords = [-2, -1, 0, 1, 2]
grid = [(x,y) 
        for x in x_coords
        for y in y_coords]
print(grid)        # all combinations 
# [(-2, -2), (-2, -1), (-2, 0), (-2, 1), ... (2, 0), (2, 1), (2, 2)]


# math.hypot , distance from the origin to a point 
# e.g. hypotenuse of a 3/4/5 right triangle is 
# >>> math.hypot(3,4)
# 5.0


# dict insert keys 
d = {'a': 1, 'b': 2}
if 'c' not in d: 
    d['c'] = 0 

# method 1 not efficient
def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value 
        return value 
    else:
        return d[key] 

# use set default method 
d.setdefault(key, value)


# common operations 
d = dict(zip('abc', range(1,4)))
print(d, len(d), d['a'])
# {'a': 1, 'b': 2, 'c': 3} 3 1
d.get('a')          # return 1 
result = d.get('python')     # will not throw exception if key not found 
print(type(result))         # <class 'NoneType'>
print(d.get('z'), 'N/A')    # default N/A if key not found 


# count chars 
text = "to be or not to be this is a question"
counts = dict()
for c in text:
    counts[c] = counts.get(c, 0) + 1    # if key not found, return 0+1
print(f"counts {counts}")
# counts {'t': 5, 'o': 5, ' ': 9, 'b': 2, 'e': 3, 'r': 1, 'n': 2, 'h': 1, 'i': 3, 's': 3, 'a': 1, 'q': 1, 'u': 1}


# count lower and upper case as same letter 
counts = dict()
for c in text:
    key = c.lower().strip()
    if key: 
        # use get() method, if key not found, set to 0, add 1, store in new key 
        counts[key] = counts.get(key, 0) + 1  
print(counts)
# {'t': 5, 'o': 5, 'b': 2, 'e': 3, 'r': 1, 'n': 2, 'h': 1, 'i': 3, 's': 3, 'a': 1, 'q': 1, 'u': 1}


#
d = dict(a=1, b=2, c=3)
'a' in d    # True 
'z' not in d   # True
d = dict.fromkeys('abcd', 0)
print(d)   
# {'a': 0, 'b': 0, 'c': 0, 'd': 0}
d.pop('a')
print(d)
# {'b': 0, 'c': 0, 'd': 0}
d.pop('b')
print(d)
# {'c': 0, 'd': 0}


#
d = dict({i: i**2 for i in range(1,5)})
print(d)
# {1: 1, 2: 4, 3: 9, 4: 16}
d.popitem()
print(d)
# {1: 1, 2: 4, 3: 9}

# 
def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value 
        return value 
    else:
        return d[key]

d = dict({i: i**2 for i in range(1,5)})
insert_if_not_present(d, 'z', 100)
print(d)
# {1: 1, 2: 4, 3: 9, 4: 16, 'z': 100}
insert_if_not_present(d, 'x', -10)
print(d)
# {1: 1, 2: 4, 3: 9, 4: 16, 'z': 100, 'x': -10}
d.setdefault('a', 100)


# import string 
print(string.ascii_lowercase)
print(string.ascii_uppercase)
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# add dict value using set.add()
categories = {}
for c in text: 
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else: 
            key = 'other'
        # if key not in categories:
        #     categories[key] = set()   # use set() to store values 
        # categories[key].add(c)    
        categories.setdefault(key, set()).add(c)  # same as above 3 lines 

for cat in categories:
    print(f'{cat}: ', ''.join(categories[cat]))
# lower:  qenisoarubth


# make above a bit clear 
def cat_key(c):
    if c == ' ':
        return None 
    elif c in string.ascii_lowercase:
        return 'lower'
    elif c in string.ascii_upper:
        return 'upper'
    else: 
        return 'other'

categories = {}
for c in text:
    key = cat_key(c)
    if key: 
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'version 2: {cat}: ', ''.join(categories[cat]))
# version 2: lower:  ubiqoasernht

# another approach 
def cat_key(c):
    categories = {' ': None, 
                string.ascii_lowercase: 'lower', 
                string.ascii_uppercase: 'upper'}
    for key in categories: 
        if c in key: 
            return categories[key]
    else: 
        return 'other'
print(cat_key('a'), cat_key('A'), cat_key(','))
# lower upper other


# use itertools.chain method 
from itertools import chain 
def cat_key(c):
    cat_1 = {' ': None}
    cat_2 = dict.fromkeys(string.ascii_lowercase, 'lower')
    cat_3 = dict.fromkeys(string.ascii_uppercase, 'upper')
    categories = dict(chain(cat_1.items(), cat_2.items(), cat_3.items()))
    # categories = (**cat_1, **cat_2, **cat_3)  # same as above
    return categories.get(c, 'other')

print('version 3', cat_key('a'), cat_key('A'), cat_key(':'))     
# version 3 lower upper other

## dictionary views 
'''
3 ways to see dict data 
keys only   d.keys()
values only d.values()
k/v pairs   d.items()

keys() view is more than an iterable, behaves like a set 
unique and hashable , required for sets 
union, intersection, difference of these key views - just like sets 

values() not behave like a set 
items() view may behave like a set 
'''

s1 = {'a', 'b', 'c'}
s2 = {'b', 'c', 'd'}
print(f"union: {s1 | s2}, intersection:  {s1 & s2}, difference: {s1 - s2}")
# union: {'a', 'c', 'd', 'b'}, intersection:  {'c', 'b'}, difference: {'a'}


# dict and sets 
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = dict(zip('cde', [10,20,30]))
for key in d1:  # by default dict iterates over keys
    print(key)
# same as above
for key in d1.keys():
    print(key)


for vavlue in d1.values():
    print(value)

# dict.keys(), values(), items() are dynamic updated 
# set has no guarantee the order 

list(d1.items()) == list(zip(d1.keys(), d1.values()))       # always True


# dict union and interaction
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a':10, 'c': 30, 'd': 40}
union = d1.keys() | d2.keys()
interaction = d1.keys() & d2.keys()

union - interaction 
# sysmetric difference , same as above line
d1.keys() ^ d2.keys()       # same as union - interaction 

# other options 
results = {}
for key in d1.keys() ^ d2.keys():
    results[key] = d1.get(key) or d2.get(key)
print(results)
# {'d': 40, 'b': 2}

# same as above 
results = {}
for key in (d1.keys() | d2.keys()) - (d1.keys() & d2.keys()):
    results[key] = d1.get(key) or d2.get(key)
print(results)
# {'b': 2, 'd': 40}

# use dict comprehension 
results = {key: d1.get(key) or d2.get(key) for key in d1.keys()^d2.keys()}
print(results)
# {'b': 2, 'd': 40}     # not ordered because using set approach to get both keys (^)

'''
dict update method - three forms 
d1.update(d2)
d1.update(iterable)     # (key, value)
d1.update(keyword-args)    # similar to dict(a=10, b=20)

d1 and d2 are two dictionaries 
for every (k, v) in d2 
    if k not in d1, inserts (k, v) in d1 
    if k in d1, updates values for k in d1   
'''

d1 = {'a':1, 'b': 2}
d2 = {'b':20, 'c': 30}
d1.update(d2)
print(f"d1: {d1}")
# d1: {'a': 1, 'b': 20, 'c': 30}

d1.update(b=20, c=30)
print(f"d1-2: {d1}")
# d1-2: {'a': 1, 'b': 20, 'c': 30}

it1 = (('b',20), ('c',30))
it2 = (('b',20), ['c',30])
it3 = [('b',20), ('c',30)]
d1.update(it1)
d1.update(it2)
d1.update(it3)
print(f"d1-it: {d1}")
# d1-it: {'a': 1, 'b': 20, 'c': 30}
# can also pass generator as iterable 
d1 = {'a':1, 'b':2}
d1.update(((k, ord(k)) for k in 'bcd'))
print(f"d1: {d1}")
# d1: {'a': 1, 'b': 98, 'c': 99, 'd': 100}

# unpacking dictionaries 
def func(**kwargs):     # d = {'a':1, 'b': 2}
    print(kwargs)       # func(**d)   -> kwargs -> {'a':1, 'b': 2}

d1 = {'a':1, 'b':2}
d2 = {'a': 10, (0,0): 'origin'}
d3 = {'b': 20, 'c': 30, 'a': 100}
d = {**d1, **d2, **d3}    # dict chaining 
print(f"unpacking: {d}")
# key order is maintained, even when updated
# unpacking: {'a': 100, 'b': 20, (0, 0): 'origin', 'c': 30}


# dict shallow copy, both k,v are shared references 
'''
shallow copies: 
container object is a new object
copied ontainer element keys/values are shared references with original objects
d_copy = d.copy()
d_copy = {**d}
d_copy = dict(d)
d_copy = {k:v for k, v in d.items()}    # slower, don't use for a simple copy

deep copies:
no shared references, even with nested dictionaries 
simpler to use copy.deepcopy 
from copy import deepcopy -> works for custom objects, iterables, dictionaries, etc
'''


# dict default values, with overlays
conf_defaults = dict.fromkeys(('host', 'port'), None)  # default None 
print(conf_defaults)
# {'host': None, 'port': None}
conf_global = {'port': 5432, 'database': 'global'}
conf_dev = {
    'host': 'localhost',
    'port': 6432
}
conf_prod = {
    'host': 'prod_host',
    'port': 7432
}
# dict unpacking is useful for env config 
# conf_defaults -> global -> dev/prod 
conf = {**conf_defaults, **conf_global, **conf_dev}    # load dev 
conf = {**conf_defaults, **conf_global, **conf_prod}    # load prod 


# 
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

p1 = Person('John', 20)
p2 = Person('John', 20)
print(p1 is p2) # False
print(p1 == p2) # False, because __eq__ is not implemented, id() is used
print(hash(p1), hash(p2))   # diff hash 8762127663041 8762127663044


# class with __eq__

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    def __eq__(self, other):    # implement __eq__ 
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age 
        else:
            return False 
    def __hash__(self):
        return hash(self.name, self.age)



# sortedd dict by keys
def sort_dict_by_value(d):
    # d = {k:v
    #     for k, v in sorted(d.items(), key=lambda el: el[1])
    # }
    # return d
    # same as above 
    return dict(sorted(d.items(), key=lambda el: el[1]))

# find unique keys in two dicts
def intersection(d1, d2):
    d1_keys = d1.keys()
    d2_keys = d2.keys()
    keys = d1_keys & d2_keys 
    d = {k: (d1[k], d2[k]) for k in keys}
    return d 


# merge dicts and sort by values
def merge(*dicts):     # take in arbitrary number of dicts 
    unsorted = {}
    for d in dicts:
        for k, v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v 
    # return unsorted
    # sort items based on dict values
    return dict(sorted(unsorted.items(), key=lambda el: el[1], reverse=True))#, reverse=False)

d1={'python': 1, 'java': 2, 'javascript': 3}
d2={'python': 5, 'c++': 6, 'javascript': 3}

print(merge(d1, d2))
# {'python': 6, 'javascript': 6, 'c++': 6, 'java': 2}


# find keys in the union but not in the intersection 
n1 = {'a': 1, 'b': 2, 'x': 10}
n2 = {'b': 2, 'c': 3, 'x': 10}
n3 = {'c': 3, 'd': 4, 'x': 10}
union = n1.keys() | n2.keys() | n3.keys()
intersection = n1.keys() & n2.keys() & n3.keys()
print(union, intersection, union-intersection)
# {'c', 'x', 'd', 'a', 'b'} {'x'} {'a', 'b', 'd', 'c'}

# build new dict of unique keys
def identify(node1, node2, node3):
    union = node1.keys() | node2.keys() | node3.keys()
    intersection = node1.keys() & node2.keys() & node3.keys()
    relevant = union - intersection
    result = {    # use comprehension, if key not found, return 0 
        key: (node1.get(key, 0), node2.get(key, 0), node3.get(key, 0))
        for key in relevant
    }
    return result 

print(identify(n1, n2, n3))
# {'a': (1, 0, 0), 'c': (0, 3, 3), 'b': (2, 2, 0), 'd': (0, 0, 4)}


## specialized dictionaries 
'''
defaultdict         automatic default values for "missing" keys 
OrderedDict         guaranteed key ordering (based on insertion order)
Counter             specialized tools for dealing with counter 
ChainMap            efficient way of "combining" multiple dictionaries
UserDict            
'''

# defaultdict   subclass of dict type, default is None
# d = defaultdict(lambda: 'python')

from collections import defaultdict 
d = {}
# d['a']   # error 
d.get('a')      # no error even not found 


# common approach
counts = {}
sentence = "hello world"
for c in sentence: 
    if c in counts:
        counts[c] += 1 
    else: 
        counts[c] = 1 
print(counts)
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


# use d.get()
counts = {}
for c in sentence:
    counts[c] = counts.get(c, 0) + 1

print(counts)       # output is same as above 


# use defaultdict 
counts = defaultdict(lambda: 0)     # default value 0
for c in sentence:
    counts[c] += 1     # we don't have to check if already exists 
                        # create new key if not found, add default value 
print(f"defaultdict: {counts}")
# defaultdict: defaultdict(<function <lambda> at 0x7f9a180bfb80>, {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

print(isinstance(counts, defaultdict))
print(isinstance(counts, dict))
print(counts.items())
# True
# True
# dict_items([('h', 1), ('e', 1), ('l', 3), ('o', 2), (' ', 1), ('w', 1), ('r', 1), ('d', 1)])

print(counts['z'])      # key not found, it will be created with default key 
print(f"counts['z']: {counts}")
# ... 'z': 0})

counts['hello'] = 'world'       # add key/value
del counts['hello']             # delete key/value 

# common seen below 
c = defaultdict(int)        # int is a callable function, a factory, not a type here 
c = defaultdict(lambda: 0)  # same as above  
print(f"int(): {int()}") 
# int(): 0
print(f"other factory calls: {bool()}, {str()}, {list()} ")
# other factory calls: False, , [] 


persons = {
    'alice': {'age': 42, "hair_color": 'brown'},
    'bob': {'age': 52, "hair_color": 'black'},
}

# extract data from dict 
hair_colors = {}
for person, details in persons.items():
    if 'hair_color' in details:
        color = details['hair_color']
    else:
        color = 'unknown'

    if color in hair_colors:
        hair_colors[color].append(person)    # append existing
    else:
        hair_colors[color] = [person]       # add color / person

print(f'hair_color: {hair_colors}')


# a slight different way 
hair_colors = {}
for person, details in persons.items():
    color = details.get('hair_color', 'unknown')   # default unknown
    person_list = hair_colors.get(color, [])
    person_list.append(person)
    hair_colors[color] = person_list 

print(f'hair_colors_2: {hair_colors}')
# hair_colors_2: {'brown': ['alice'], 'black': ['bob']}


# use defaultdict 
hair_colors = defaultdict(list)
for person, details in persons.items():
    color = details.get('hair_color', 'unknown')
    hair_colors[color].append(person)
print(f'hair_colors_defautdict: {hair_colors}')
# defaultdict(<class 'list'>, {'brown': ['alice'], 'black': ['bob']})


#
from functools import partial 
# below two lines have same effects
hairdict = partial(defaultdict, lambda: 'unknown')
# hairdict = lambda *args, **kwargs: defaultdict(lambda: 'unknown', *args, **kwargs) 


##
persons = {
    'alice': hairdict(age=20, hair_color='brown'),
    'bob': hairdict(age=52, hair_color='black')
}

hair_colors = defaultdict(list)
for person, details in persons.items():
    hair_colors[details['eye_color']].append(person)

print(f'hairdict: {hair_colors}')
# hairdict: defaultdict(<class 'list'>, {'unknown': ['alice', 'bob']})

# defaultdict can be handy, and simply code 
# use defaultdict for stats 
from collections import defaultdict, namedtuple 
from datetime import datetime 
from functools import wraps 

def function_stats():
    d = defaultdict(lambda: {"count": 0, "first_called": datetime.utcnow()})
    Stats = namedtuple('Stats', 'decorator data')

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            d[fn.__name__]['count'] += 1    # key fn.__name__
            return fn(*args, **kwargs)
        return wrapper 

    return Stats(decorator, d)    # namedtuple 


stats = function_stats()    # define an object 
stats.data 

@stats.decorator 
def func_1(): 
    pass 

@stats.decorator 
def func_2(x, y):
    pass 

func_1()
print(stats.data)
# defaultdict(<function function_stats.<locals>.<lambda> at 0x7f78f801ae50>, {'func_1': {'count': 1, 'first_called': datetime.datetime(2023, 4, 10, 22, 36, 2, 595408)}})

func_2(10,20)
print(stats.data)
# defaultdict(<function function_stats.<locals>.<lambda> at 0x7f92b8102e50>, {'func_1': {'count': 1, 'first_called': datetime.datetime(2023, 4, 10, 22, 36, 35, 263596)}, 'func_2': {'count': 1, 'first_called': datetime.datetime(2023, 4, 10, 22, 36, 35, 264216)}})


# > python 3.6, dict keeps insertion order 
from collections import OrderedDict
d1 = OrderedDict(a=1, b=2, c=3, d=4)
d2 = dict(a=1, b=2, c=3, d=4)

first_key = next(iter(d2.keys()))
print(d2)
print(first_key)


def popitem(d, last=True):
    if last:
        return d.popitem()
    else:
        first_key = next(iter(d.keys()))
        return first_key, d.pop(first_key)

d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
print(popitem(d2))   # pop last item 
print(d2)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# ('d', 4)
# {'a': 1, 'b': 2, 'c': 3}


d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
print(popitem(d2, last=False))   # pop first item 
print(d2)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# ('a', 1)
# {'b': 2, 'c': 3, 'd': 4}


d = dict(a=1, b=2, c=3, d=4)
key = 'c'
print(d.keys())
d[key] = d.pop(key)
print(d.keys())

keys = list(d.keys())[:-1]
for key in keys:
    d[key] = d.pop(key)    # add key/value back to dict 
    print(d.keys())

print(d)
# dict_keys(['a', 'b', 'c', 'd'])
# dict_keys(['a', 'b', 'd', 'c'])
# dict_keys(['b', 'd', 'c', 'a'])
# dict_keys(['d', 'c', 'a', 'b'])
# dict_keys(['c', 'a', 'b', 'd'])
# {'c': 3, 'a': 1, 'b': 2, 'd': 4}

#
def move_to_end(d, key, *, last=True):
    d[key] = d.pop(key)

    if not last: 
        for key in list(d.keys())[:-1]:
            d[key] = d.pop(key)

d = dict(a=1, b=2, c=3, d=4)
move_to_end(d, 'c')
print(d)
# {'a': 1, 'b': 2, 'd': 4, 'c': 3}

move_to_end(d, 'b', last=False)
print(d)
# {'b': 2, 'a': 1, 'd': 4, 'c': 3}

# compare 2 dicts 
def dict_equal_sensitive(d1, d2):
    if d1 == d2: 
        for k1, k2 in zip(d1.keys(), d2.keys()):
            if k1 != k2: 
                return False 
        return True 
    else: 
        return False 


# use all() to compare 2 dicts 
def dict_equal_sensitive2(d1, d2):
    if d1 == d2: 
        return all(k1 == k2 for k1, k2 in zip(d1, d2))
    else:
        return False 


# use map() to compare 2 dicts 
def dict_equal_sensitive(d1, d2):
    if d1 == d2: 
        return all(map(lambda el: el[0] == el[1], zip(d1, d1)))
    else:
        return False 


# use Dictionary to maintain Counters
"""
d = {}
d[key] = d.get(key, 0) + 1

d = defaultdict(int)
d[key] += 1 

collections.Counter class 
acts like a defaultdict and with a default of 0 

"""

# Counter 
from collections import defaultdict, Counter 
sentence = 'the quick brown fox jumps over the lazy doc'
counter = defaultdict(int)
for c in sentence:
    counter[c] += 1 
print(counter)    
# defaultdict(<class 'int'>, {'t': 2, 'h': 2, 'e': 3, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 2, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1})

# use built-in Counter()
counter = Counter()
for c in sentence:
    counter[c] += 1 

print(counter) 
# Counter({' ': 8, 'o': 4, 'e': 3, 't': 2, 'h': 2, 'u': 2, 'c': 2, 'r': 2, 'q': 1, 'i': 1, 'k': 1, 'b': 1, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1})

# count random numbers 
import random 
random.seed(0)
my_list = [random.randint(0, 10) for _ in range(1_000)]
c2 = Counter(my_list)
print(c2)
# Counter({1: 107, 10: 98, 0: 97, 6: 95, 7: 94, 4: 91, 5: 89, 2: 88, 9: 85, 3: 80, 8: 76})


import random 
random.seed(0)
my_list = [random.randint(0, 10) for _ in range(1_000)]
c2 = my_list = Counter(my_list)
print(f"c2: {c2}")
# c2: Counter({1: 107, 10: 98, 0: 97, 6: 95, 7: 94, 4: 91, 5: 89, 2: 88, 9: 85, 3: 80, 8: 76})

c3 = Counter(a=1, b=2)
print(c3)
# Counter({'b': 2, 'a': 1})


# split words 
import re 
sentence = "In the face of ambiguity, refuse the temptation to guess"
words = re.split('\W', sentence)
print(type(words), words)
# <class 'list'> , ['In', 'the', 'face', 'of', 'ambiguity', '', 'refuse', 'the', 'temptation', 'to', 'guess']

word_count = Counter(words)
print(f'word_count: {word_count}')
# word_count: Counter({'the': 2, 'In': 1, 'face': 1, 'of': 1, 'ambiguity': 1, '': 1, 'refuse': 1, 'temptation': 1, 'to': 1, 'guess': 1})

print(f'top 3 common: {word_count.most_common(3)}')
# top 3 common: [('the', 2), ('In', 1), ('face', 1)]


c1 = Counter('abba')
print(f'c1: {c1}')
# c1: Counter({'a': 2, 'b': 2})


for c in c1.elements():
    print(f'c: {c}')
# c: a
# c: a
# c: b
# c: b


l = []
for i in range(1, 5):
    for _ in range(i):
        l.append(i)
print(l)
# [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]


c1 = Counter()
for i in range(1,11):
    c1[i] = i 
print(f'c1: {type(c1)} {c1}')   
# c1: <class 'collections.Counter'> Counter({10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2, 1: 1}) 

# c1.elements() - Iterator over elements repeating each as many times as its count.
print(type(c1.elements()))

# <class 'itertools.chain'>
print(list(c1.elements()))   
# [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

class RepeatIterable: 
    def __init__(self, **kwargs):
        self.d = kwargs 
    
    def __setitem__(self, key, value):
        self.d[key] = value 

    def __getitem__(self, key):
        self.d[key] = self.d.get(key, 0)
        return self.d[key]

    def elements(self):
        for k, frequency in self.d.items():
            for _ in range(frequency):
                yield k 

r = RepeatIterable(a=2, b=3, c=1)
for e in r.elements():
    print(f'e: {e}')
# e: a
# e: a
# e: b
# e: b
# e: b
# e: c    

r = RepeatIterable(x=10, y=20)
print(f'r.d: {r.d}')
# r.d: {'x': 10, 'y': 20}


# Counter update 
c1 = Counter(a=1, b=2, c=3)
c2 = Counter(b=1, c=2, d=3)
c1.update(c2)
print(f'c1: {c1}')
# c1: Counter({'c': 5, 'b': 3, 'd': 3, 'a': 1})


c1 = Counter(a=1, b=2, c=3)
c2 = Counter(a=1, b=2, c=3)
c1.subtract(c2)
print(f'c1: {c1}')
# c1: Counter({'a': 0, 'b': 0, 'c': 0})
c1.subtract(c2)
print(f'c1: {c1}')
# c1: Counter({'a': -1, 'b': -2, 'c': -3})

# minimum, maximum, 
c1 = Counter(a=5, b=1)
c2 = Counter(a=1, b=10)
print(f'c1 & c2: {c1 & c2}')
# c1 & c2: Counter({'a': 1, 'b': 1})

print(f'c1 | c2: {c1 | c2}')
# c1 | c2: Counter({'b': 10, 'a': 5})

# find positive values only 
c1 = Counter(a=10, b=-10, c=0)
print(f'c1: {c1}')
print(f'+c1: {+c1}')
# +c1: Counter({'a': 10})     #get positive values only 


# ChainMap
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = {**d1, **d2, **d3}
print(d)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# same as below 
d = {}
d.update(d1)
d.update(d2)
d.update(d3)
print(d)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


from collections import ChainMap 

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

d = ChainMap(d1, d2, d3)
print(d, isinstance(d, dict))
# ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}) False
print(d['a'], d['e'])
# 1 5


for k, v in d.items():
    print(k, v)
# 1 5
# e 5
# f 6
# c 3
# d 4
# a 1
# b 2    


# UserDict , custom dict 
from numbers import Real 

class IntDict: 
    def __init__(self):
        self._d = {}
    
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Value must be a real number.')
        self._d[key] = value 

    def __getitem__(self, key):
        return int(self._d[key])

d = IntDict()
d['a'] = 10.5
print(d['a'])

# ValueError: Value must be a real number.
# d['b'] = 2 + 3j
# print(d)


class IntDict(dict):
    def __init__(self):
        self._d = {}

    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Value must be a real number')
        self._d[key] = value 

    def __getitem__(self, key):
        return int(self._d[key])        


d = IntDict()
d['a'] = 10.5
print(f"d['a']: {d['a']}")
# d['a']: 10   # get integer portion back, not truncated 

# use dict inheritance, get a lot of functionalities 
class IntDict(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Values must be a real number')
        super().__setitem__(key, value)

    def __getitem__(self, key):
        return int(super().__getitem__(key))

d = IntDict()
d['a'] = 11.5
# inherit functions from super class 
print(d['a'], d.get('a'), d.items(), d.keys(), d.values(), d.get('x', None))
# 11 11.5 dict_items([('a', 11.5)]) dict_keys(['a']) dict_values([11.5]) None


from collections import UserDict 
# help(UserDict)


# normal zip,combine shortest of list
l1 = ['a', 'b', 'c']
l2 = [1, 2, 3, 4]
print(list(zip(l1, l2)))
[('a', 1), ('b', 2), ('c', 3)]


# zip longest with default value 
from itertools import zip_longest 
print(list(zip_longest(l1, l2, fillvalue="??")))
# [('a', 1), ('b', 2), ('c', 3), ('??', 4)]


# 3.10, zip introduce strict flag 
l1 = (i ** 2 for i in range(4))
l2 = (i ** 3 for i in range(3))
# result = zip(l1, l2, strict=True)
# error zip lists of different length 
# result = zip(l1, l2, strict=True)
# TypeError: zip() takes no keyword arguments
