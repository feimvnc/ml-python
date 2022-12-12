# generators functions can return objects which can be 
# iterated over, generate items inside the object lazily 
# can generate the items only one at a time
# only when you ask for it 
# much more memory efficient than other sequence objects 
# when to deal with large data sets 
# defined like normal function, but with yield keyword instead of return keyword

def mygenerator():
    yield 1
    yield 2 
    yield 3

g = mygenerator()

for i in g:
    print(i)
# 1
# 2
# 3

g = mygenerator()
v = next(g)
print(v)    # print 1 
v = next(g)
print(v)    # print 2  
v = next(g)
print(v)    # print 3
# v = next(g)
# print(v)       # error StopIteration 

# use iterables 
g = mygenerator()
print(sum(g))   # print 6 

g = mygenerator()
print(sorted(g))

#
def countdown(num):
    print('Starting')
    while num > 0: 
        yield num 
        num -= 1 

cd = countdown(4)
value = next(cd)

print(value)

print(next(cd))
print(next(cd))
print(next(cd))
# print(next(cd))   # error StopIteration

# generator is memory efficient, save memory for large data 
# memory comparison between list and generator 
import sys 
def firstn(n):
    nums = []   # list needs memory allocation 
    num = 0 
    while num < n:
        nums.append(num)
        num += 1 
    return nums 

def firstn_generator(n):
    num = 0 
    while num < n: 
        yield num 
        num += 1 

print(sum(firstn(10)))      # 45 
print(sum(firstn_generator(10)))    # 45
print(sys.getsizeof(firstn(10)))    # 184 
print(sys.getsizeof(firstn_generator(10)))  # 112 
print(sys.getsizeof(firstn(1000000)))    # 8448728 
print(sys.getsizeof(firstn_generator(1000000)))  # 112 

# fibonacci sequence 
def fibonacci(number):
    # 0 1 1 2 3 5 8 13 ...
    a, b = 0, 1 
    while a < number: 
        yield a 
        a, b = b, a + b 

fib = fibonacci(30)
for i in fib:
    print(i)

# generator expression 
# written like list compressions 
# but with parenthesis brackets 

import sys 
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))       # 112

mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist))        # 4216


