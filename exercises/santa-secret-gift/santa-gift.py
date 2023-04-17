#tested at below 
# https://coderpad.io/resources/docs/for-candidates/interview-preparation-guide/sandbox/i

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

