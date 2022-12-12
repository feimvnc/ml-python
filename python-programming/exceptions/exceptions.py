# errors and exception
# program returns errors or exception due to exception or syntax error 

#a = 5 print(5) # syntax error
#a = 5 
#print(a))   # syntax error
#a = 5 + '10'    # type error
# import somemodule # module not found error 
# f = open('filenotfound.txt') # file not found error 

a = [1,2,3]
#a[4]    # index error

dict = {"name":"alice"}
# dict['age'] # key error

# raise exception
x = -1 
# if x < 0:
#     raise Exception('x should be positive') #Exception: x should be positive

# assert(x>=0), 'x should >= 0' # return True if match ,AssertionError

# catch exception 
try:
    a = 5/0
# except Exception as e:
    # print('error divide by 0')
    # print(e)
except ZeroDivisionError as e :
    print(e)
except TypeError as e:
    print(e)
else: 
    print("no exception")
finally: 
    print("cleaning up...")  # always run 

class ValueTooHighError(Exception):
    pass 

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message 
        self.value = value 

def test_value(x):
    if x >100 :
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value too small', x)
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)

