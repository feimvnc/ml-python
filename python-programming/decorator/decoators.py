# there are two decorators 
# function decorators, class decorators 

# extend function without change function code 
# allow you to add new functionalities  
# 
# @mydecorator    
# def dosomething():
#     pass  

def start_end_decorator(func):

    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

def print_name():
    print('Alice')

#print_name()
#use decorator 
print_name = start_end_decorator(print_name)
print_name()
# print out 
# start
# Alice
# end

@start_end_decorator        # same effect 
def print_name():
    print('Alice')
print_name()

import functools 
# decorator pass args and return value
def decorator_with_args(func):
    @functools.wraps(func)  # serve func informationn
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('end')
        return result 
    return wrapper 

@decorator_with_args
def add5(x):
    return x + 5 

result = add5(10)
print(result)   # print 15 

# print type 
print(help(add5))
print(add5.__name__)    
# print wrapper without functool
# print add5 with functool 

# decorator with args 
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result 
        return wrapper 
    return decorator_repeat

@repeat(num_times=2)
def greet(name):
    print(f'Hello {name}')

greet('Alice')
# output print twice 
# Hello Alice
# Hello Alice

# apply multiple decorators 
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result 
    return wrapper 

def start_end_decorator_new(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result 
    return wrapper 

@debug 
@start_end_decorator_new 
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting 

say_hello('Alice-Bob')


# apply class decorator 
# help you to maintain or update states 

class CountCalls:

    def __init__(self, func):
        self.func = func 
        self.num_calls = 0 
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1 
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls     # track how many times the class is called 
def say_hello():
    print('Hello')

say_hello() #This is executed 1 times
say_hello() #This is executed 2 times
