# lambda arguments: expression  # take argument, evaluate, return result 
# small one line function 

from audioop import mul


add10 = lambda x: x+10
print(add10(5)) # print 15 

# same as normal function 
def add10_func(x):
    return x + 10 

mult = lambda x,y: x*y 
print(mult(2,5))

points2D = [(1,8), (3,4), (2,3), (6,8)]
points2D_sorted = sorted(points2D)

print(points2D)
# sorted by first value 
print(points2D_sorted)  # [(1, 2), (2, 3), (3, 4), (6, 8)]

points2D_sorted_by_2nd_value = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted_by_2nd_value)

def sort_by_y(x):
    return x[1]

# use normal func 
points2D_sorted_by_2nd_value = sorted(points2D, key=sort_by_y)

# sorted by sum of tuples 
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sorted)  # sorted by sum 

# map(func, seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))  #[2, 4, 6, 8, 10]

c = [x*2 for x in a]
print(c)    # same as above lambda 

# filter function, return True only if match 
b = filter(lambda x: x%2==0, a)
print(list(b))  #[2, 4]

# same as above 
c = [x for x in a if x%2==0]
print(c)    #[2, 4]

# reduce return single value 
from functools import reduce 
a = [1,2,3,4]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)    #24

