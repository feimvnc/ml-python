# enumerate function: loop with counters 
# list.index(n) is an expensive call, traverse the for-loop twice
# enumerate allows to loop through list, tuple, dictionay, stings and gives index 
# takes in a data collection as a parameter and 
# adds counter to an interable and returns it 
# enumerate(iterable, start)
# enumerate(iterable, start=0)


a = list(range(10))
enum_a = enumerate(a)   # return key/value pairs 
print(list(enum_a))    
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]

print((enum_a))
#  <enumerate object at 0x7fca081a7bc0>

enum_a = enumerate(a, 10)  # change the default counter from 10
print(list(enum_a))  
# [(10, 0), (11, 1), (12, 2), (13, 3), (14, 4), (15, 5), (16, 6), (17, 7), (18, 8), (19, 9)]

# loop through an enumerate object 
a = list(range(10))
enum_a = enumerate(a)
for item in enum_a:
    print(item)
'''
(0, 0)
(1, 1)
(2, 2)
...
'''    

# convert enum to list 
a = list(range(10))
enum_a = enumerate(a)
print(f"list enum_a: {list(enum_a)}")
# list enum_a: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]

# print counter and value 
a=['a', 'b', 'c']
for index, value in enumerate(a):
    print(f"index, value: {index}, {value} ")
'''
index, value: 0, a 
index, value: 1, b 
index, value: 2, c
'''

a=['a', 'b', 'c']
list_a = a 
print(list_a)   # ['a', 'b', 'c']


# enumerate alternatives 
def remove_every_other(lst):    # use enum
    result = []
    for i, val in enumerate(lst):
        if i % 2 == 0:
            result.append(val)
    return result 

def remove_every_other_listcomp(lst):
    return [ i for i in lst if i % 2 != 0]


# much simpler form 
lst = list(range(10))
new_lst = lst[::2]    

# zip function 
a = list(range(5))
print(f"zip: {list(zip(range(len(a)), a))}")
# zip: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# map function
a = list(range(5))
print(f"map: {list(map(lambda x: (x, a[x]), range(len(a))))}")
# map: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# list comprehension 
a = list(range(5))
print(f"list_comp: {[(x, a[x]) for x in range(len(a))]}")
# list_comp: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# multiple list
a = list(range(5))
b = list(range(10, 5))
c = list(range(100, 5))
for i, (i,j,k) in enumerate(zip(a,b,c)):
    print(i, i,j,k)

# enumerate in range 
a = list(range(10))
print([i for i, x in enumerate(a) if 3 <= x <=8])
# [3, 4, 5, 6, 7, 8]