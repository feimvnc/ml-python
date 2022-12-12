# itertools: product, permutations, combinations, 
# accumulate, groupby, and infinite iterations 

from itertools import product
from math import prod
a = [1,2]
b = [3,4]
prod = product(a, b)
print(list(prod))   #[(1, 3), (1, 4), (2, 3), (2, 4)]

a = [1,2]
b = [3]
c = product(a, b, repeat=2)
print(list(c))

from itertools import permutations 
a = [1,2,3]
p = permutations(a)
print(list(p))


p = permutations(a, 2)  # length of 2 
print(list(p))

from itertools import combinations 
a = [1,2,3]
c = combinations(a, 2)  # 2nd value length is required
print(list(c))

# combinations_with_replacement 
from itertools import combinations, combinations_with_replacement 
a = [1,2,3,4]
cr = combinations_with_replacement(a, 2)
(a, 2)
print(list(cr))

# accumulate , return sum 
from itertools import accumulate 
a = [1,2,3]
acc = accumulate(a)
print(a)    #[1, 3, 6]

import operator
a = [1,2,3,4]
acc = accumulate(a, func=operator.mul)
print(list(acc))    # [1, 2, 6, 24]

# return max of each comparison
a = [1,2,5,3,4]
acc = accumulate(a, func=max) 
print(list(acc))  

from itertools import groupby
def smaller_than_3(x):
    return x < 3 
 
a = [1,2,3,4,5]
group_obj = groupby(a, key=smaller_than_3)
for k, v in group_obj:
    print(k,list(v))
# True [1, 2]
# False [3, 4, 5]

a = [1,2,3,4,5]
# use lambda to do have same result 
group_obj = groupby(a, key=lambda x: x<3)
for k, v in group_obj:
    print(k,list(v))

# group by dict key 
persons = [{'name': 'alice', 'age': 10},
            {'name': 'bob', 'age': 10},
            {'name': 'charlie', 'age': 15},
            {'name': 'dav', 'age': 12}]
group_obj = groupby(persons, key=lambda x: x['age'])
for k, v in group_obj:
    print(k, list(v))
# 10 [{'name': 'alice', 'age': 10}, {'name': 'bob', 'age': 10}]

from itertools import count, cycle, repeat 
for i in count(10):
    print(i)
    if i == 15:
        break   # stop at 15 

a = [1,2,3]
for i in cycle(a):  # cycle 3 times 
    print(i)
    if i == 3:
        break   # stop at 15 

for i in repeat(1, 4): # repeat 4 times 
    print(i)