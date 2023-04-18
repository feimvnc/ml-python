#tested at below 
# https://coderpad.io/resources/docs/for-candidates/interview-preparation-guide/sandbox/i

## method 1
from typing import List
def say_hello(l: List) -> List:
    #print('Hello, World')
    import numpy as np
    l = list('abcdef')
    print(l)
    np.random.shuffle(l)
    print(l)
    res = []
    for (i, j) in zip(l[::-1], l):
        res.append([i, j])
    return res

l = list('abcdef')
#for i in range(5):
print(f"name list is: {say_hello(l)}")



## method 2
import random
def say_hello():
    print('Hello, World')
    a = list("abcdef")
    b = random.sample(a, k=len(a))
    b_2 = b[::-1]
    results = [[i, j] for (i, j) in zip(b, b_2)]
    for item in results: 
        #print(item[0], item[1])
        if item[0] == item[1]:
             print("error, rule broken")
             break
    print(results)
    #help(random)

for i in range(10):
    say_hello()





