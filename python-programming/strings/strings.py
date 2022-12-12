# Strings: orderedd, immutable, text representation 
# most used datatype in python

# can use both "" or ''
s = "hello"
s1 = 'world'        # "I'm", or "I'm", this is valid
print(s)
print(s1)

# """ """, triple quotes for multiple lines 
s3 = """hello
world"""

char = s[-1]
print(char) # 'o' 

char = s[-2]
print(char) # 'l' 

# sting does not support item assignment 
# s[0] = 'X'
# print(s)    #TypeError: 'str' object does not support item assignment

#substring 
s4 = "Hello World"
substring = s4[1:5] #ello
print(substring)

substring = s4[:4]  # Hell
print(substring)

substring = s4[::2]  # HloWrd
print(substring)

substring = s4[::-1]  # dlroW olleH
print(substring)

# cat string 
greeting = "Hello"
name = "Alice"
sentence = greeting + " " + name 
print(sentence)

# print letters
for i in greeting:
    print(i)

# 
if 'elle' in greeting: 
    print('yes')
else: 
    print('no')

# strip empty space 
s5 = '   Hello World   '
s5 = s5.strip()
print(s5)  #Hello World

s6 = '   Hello World   '
s6.strip()  # empty space not removed 
print(s6)  #Hello World

s6 = '   Hello World   '
s6_copy = s6.strip()
print(s6_copy)  #Hello World
print(s6_copy.lower())  #hello world
print(s6_copy.upper())  #HELLO WORLD
print(s6.startswith('World'))   #False
print(s6.endswith('World   '))     #True
print(s6.find('ld'))    #12 , index
print(s6.find('pp'))    #-1 , index 
print(s6.count('o'))    # 2
print(s6.replace('World', 'Universe'))  #Hello Universe  

ss = "i like to code with python"
ss1 = s.split()
print(ss1)   #['i', 'like', 'to', 'code', 'with', 'python']


ss = "i,like,to,code,with,python"
ss2 = ss.split(",")
print(ss2)  #['i', 'like', 'to', 'code', 'with', 'python']

ss3 = ''.join(ss)
print(ss3)  #i,like,to,code,with,python

ss4 = ' '.join(ss3) 
print(ss4)

ss5 = ['a']*6
print(ss5)  # ['a', 'a', 'a', 'a', 'a', 'a']

# bad code  
ss6 = ''
for i in ss5: 
    ss6 += i
print(ss6)  #aaaaaa

# good 
ss7 = ''.join(ss5)
print(ss7)      # aaaaaa

# compare time 
from timeit import default_timer as timer 

# bad 
l = ['a']*10000
# bad 
start = timer()
my_string = ''
for i in l:
    my_string += i 
stop = timer()
print(stop-start)   # 0.002140411000000002

# good 
start = timer()
my_string = ''.join(l)  # dot.join 
stop = timer()
print(stop-start)   #0.00010491400000000456

# %, .format(), f-Strings 
var = "Alice"   # %s for string 
s = "the variable is %s" %var   #the variable is Alice
print(s)

var = 5     # %d for number
s = "the variable is %d" %var   #the variable is Alice
print(s)

var = 3.14125
s = "the variable is %f" %var   # the variable is 3.141250
print(s)

s = "the variable is %.2f" %var   # the variable is 3.14
print(s)

# dot format 
s = "the variable is {}".format(var)
print(s)

s = "the variable is {:.2f}".format(var)    #3.14
print(s)

var2 = 42
s = "the variable is {:.2f} and {}".format(var, var2)    #3.14 and 42
print(s)

s = f"the variable is {var} andd {var2}"
print(s)

s = f"the variable is {var*2} andd {var*3}"
print(s)

