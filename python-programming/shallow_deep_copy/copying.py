# shallow and deep copy of objects, 
# how to make actual copies of custom objects 
# shallow copy: one level deep, only references of nestedd child objects 
# deep copy: full inddependent copy 

# use assignment operator, both points to same reference 
a = 5 
b = a  # both a and b points to same number 

b = 6   # new assignment with new value 
print(a)    # 5
print(b)    # 6 

# list immutable type, change on copy also changes on original 
l = [1,2,3]
l_copy = l 
l_copy[0] = 0
print(l)        #[0, 2, 3]
print(l_copy)   #[0, 2, 3]

# shallow copy object 
import copy 
l_copy = copy.copy(l)
# l_copy = l.copy()   # list function, also works
# l_copy = list(l)    #list function, also works
# l_copy = l[:]   # slice copy, also works

l_copy[0] = -1
print(l)        #[0, 2, 3]
print(l_copy)   #[-1, 2, 3]

# nestedd list copy 
a = [[1,2,3],[4,5,6]]
a_copy = copy.copy(a)   # shallow copy only at one level
a_copy[0][1] = -1  # this changes both a and a_copy 
print(a)        # [[1, -1, 3], [4, 5, 6]]
print(a_copy)   # [[1, -1, 3], [4, 5, 6]]

# deep copy works for nested object 
import copy 
d = [[1,2,3],[4,5,6]]
d_copy = copy.deepcopy(d)
d_copy[0][1] = -10
print(d)        # [[1, 2, 3], [4, 5, 6]]
print(d_copy)   # [[1, -1, 3], [4, 5, 6]]

# for built-in types, list, dict, tuples, use deep copy 
# can also use for custom objects 

import copy 

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

p1 = Person('Alice', 20)
p2 = copy.copy(p1)  # shallow copy, original not affected

p2.age = 28 
print(p1.age)
print(p2.age)

# add another class 
class Company:
    def __init__(self, manager, employee):
        self.manager = manager 
        self.employee = employee 

p1 = Person('Bob', 30)
p2 = Person('Joe', 25)

company = Company(p1, p2)
company_copy = copy.copy(company) # shallow copy 
company_copy.manager.age = 56 
print(company_copy.manager.age) # same 56
print(company.manager.age)      # same 56 , shallow reference, updated both

company = Company(p1, p2)
company_deep_copy = copy.deepcopy(company)
company_deep_copy.manager.age = 57
print(company_deep_copy.manager.age) # same 57, deep copy changed copy value only 
print(company.manager.age)      # same 56 , 
