def print_name(name):   # parameter 
    print(name)

print_name("Alice")     # argument 

def foo(a,b,c):
    print(a,b,c)

foo(a=1, b=2, c=3)  # keyword argument 

# better use keyword argument, it is clear, readable 
foo(c=1, b=2, a=3)  # print diff order, position not matter 

def bar(a,b,c=4):  # c default value , must at end 
    print(a,b,c)

bar(1,2)

def caz(a,b,*args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

caz(1,2,3,4,six=6,seven=7)
# six 6
# seven 7

# force keyword argument 
def fooa(a,b,*,c,d): # after * must use keyword 
    print(a,b,c,d)

fooa(1,2,c=3,d=4)

def foob(*args, last):
    for arg in args:
        print(arg)
    print(last)

foob(1,2,3, last=10)

# unpack variables 
def fooc(a,b,c):
    print(a,b,c)
my_list = [0,1,2]
fooc(*my_list)  # unpack 0,1,2 => a,b,c, length must match 

# map unpacking 
def food(a,b,c):
    print(a,b,c)
my_dict = {'a':1, 'b':2, 'c': 3}
food(**my_dict)  # keyname and length must match 

# local vs. global variables 
def fooe():
    global number 
    number = 3 

number = 0 
fooe ()
print(number)

# parameter passing, call by value or call by reference 
# python is call by object reference 
 
def fool(a_list):
    a_list.append(4)
    a_list[0]=100

my_list = [1,2,3]
fool(my_list)
print(my_list)  #[100, 2, 3, 4]

def fooh(a_list):
    a_list = a_list + [10,20,30]    # local a_list, not change outside a_list 

my_list = [1,2,3]
foo(my_list)
print(my_list)