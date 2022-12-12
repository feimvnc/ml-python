import random 

a = random.randint(1,10)
# a = random.randrange(1,10)    # upper bound not included 
print(a)

a = random.normalvariate(0, 1)  # normal distribution 
print(a)

mylist = list("abcdefg")
a = random.sample(mylist, 3)    # pick unique 3 elements 
a = random.choices(mylist, k=3)     # pick 3 elements, can have duplicate element
a = random.shuffle(mylist)      # shuffle items 

# re-produce data with random seed 
random.seed(1)
print(random.random())
print(random.randint(1,10))

# above pseudo number not suitiable for secrets , secret tokens 
# use secrets module 
import secrets 

a = secrets.randbelow(10)       #3
a = secrets.randbits(4)     # random number from 0 - 15  

mylist = list("abcdefg")
a = secrets.choice(mylist)  # random choice of value 

# can also use numpy module for random values 
import numpy as np 
a = np.random.randint(0, 10, (3,4))  # 3 by 4 dimensions 
print(a)

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)

# use seed to produce same array 
np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))

