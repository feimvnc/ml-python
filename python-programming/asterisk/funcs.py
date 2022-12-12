result = 2*3 
print(result)

v_power = 2 ** 3
print(v_power)  # 8

zeros = [0] * 10 
print(zeros)  # list of 10 elements 

zero_ones = [0,1] * 10 # works for "ab", tuple (a,b)
print(zero_ones)
# [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

def foo(a, b, *args, **kwargs):
# def foo(a, b, *, c):  # c must keyword only after *
    print(a)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1,2,3,4,5, six=6)

# unpack list, set, dict 
# unpack dictionary with **
def bar(a,b,c):
    print(a,b,c)

my_dict = {'a':1, 'b':2, 'c': 3} # key must match name 
foo(**my_dict)

# unpack 
numbers = [1,2,3,4,5]
*beginning, last = numbers 
# beginning, *middle, last = numbers 
# beginning, *middle, secondlast, last = numbers 
print(beginning)    # unpack 1,2,3,4
print(last)

# new merged list 
my_tuple = (1,2,3)
my_list = [4,5,6]
my_set = {7,8,9}
new_list = [*my_tuple, *my_list, *my_set]
print(new_list)  # [1, 2, 3, 4, 5, 6, 8, 9, 7]

# merge dict with **
dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd':4}
my_dict={**dict_a, **dict_b}
print(my_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


