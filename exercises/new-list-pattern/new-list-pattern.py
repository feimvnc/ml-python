from typing import List 
def say_hello(step: int):
    print('Hello, World')
    l = [i for i in range(1,11)]
    res = []
    while len(l) > step:
        res.extend(l[::step])
        del l[::step]
    res.extend(l)
    print(res)

for i in range(1):
    say_hello(3)

"""
n = size of list 
Time complexity: O(n)
Memory complexity: O(n+n)

-read orig list 
-create new list to store filtered result 
-delete used values from orig list
-return new list 
"""
