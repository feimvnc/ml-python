# sets: unordered, mutable, no duplicates 

from xml.etree.ElementTree import fromstring


s = {1, 2, 3}  # just separated by comma 
print(s)

s = {1, 2, 3, 1, 2}  # print same 1, 2, 3, not allow duplicates  
print(s)

s1 = set("hello")
print(s1)   # set is unordered, print {'e', 'o', 'l', 'h'}, only one 'l'

# create empty set , s3={}, => this is dict type 
s3 = set()
print(type(s3))

# add and remove 
s3.add(1)
s3.add(2)
s3.add(3)
print(s3)
# remove
s3.remove(3)
# s3.remove(4)    # keyError: 4, when key not exists
print(s3)

# discard same as remove, but no error if key not exist 
s3.discard(4)
print(s3)

# pop()
print(s3.pop())     # return one and also remove one from set 
print(s3)

# clear to clear set 
s3.clear()
print(s3)

# iterate set 
for i in s:
    print(i)

# check if value exists 
if 1 in s:
    print("yes")

# union and intersection 
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7,}

# union
u = odds.union(evens)
print(u)

# intersection, only in both sets 
i = odds.intersection(evens)    # this return empty set 
print(i)

i = odds.intersection(primes)    # this return values in both sets 
print(i)

# calculate diff of two sets, return values in s1, but not s3 
sa = {1,2,3,4,5}
sb = {1,2,3,8,9}
diff = sa.difference(sb)
print(diff)

diff = sb.difference(sa)    # return unique from set b
print(diff)

# systemtric_difference => return unique in both sets
diff = sb.symmetric_difference(sa)
print(diff)

# add element found in other set 
sa.update(sb)
print(sa)

# update set with values found in both sets 
sa.intersection_update(sb)
print(sa)

# difference_update, remove elements found in other set 
sa = {1,2,3,4,5}
sb = {1,2,3,8,9}
sa.difference_update(sb)
print(sa)

# only update sa with diff values, not common 
sa.symmetric_difference_update(sb)
print(sa)

# check if is a subset 
print(sa.issubset(sb))

# check if it is superset 
print(sb.issuperset(sa))

# disjoint, return True if two sets have a null intersection 
print(sa.isdisjoint(sb))

# set copy is by reference, so be careful 
sa = {1,2,3}
sb = sa # sb and sa have same memory address 

sc = sa.copy()  # make actual copy 
sc = set(sa)    # 2nd way to make actual copy 

# frozen set, an ummutable set of a normal set 
a = frozenset([1,2,3,4,5])
# a.add(2)        # throw error
# a.remove(2)       # throw error 



