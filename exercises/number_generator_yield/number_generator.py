from typing import List 
def say_hello():
    print('Hello, World')

    #l = []
    def gen():
        for i in range(0, 10):
        # l.extend([i, i+1, i+2, i])
        # l.append(i+1)
        # l.append(i+2)
        # l.append(i+1)
            yield i 
            yield i+1 
            yield i+2 
        #print(l)

    res = []
    for item in gen():
        res.append(item)
    print(res)

for i in range(1):
    say_hello()

