# collections: Counter, namedsuple, OrderedDict, ddefaultdict, deque

from collections import Counter 
a = "aaabbbccc"
my_counter = Counter(a)
print(my_counter)   #Counter({'a': 3, 'b': 3, 'c': 3})
print(my_counter.keys())    # dict_keys(['a', 'b', 'c'])
print(my_counter.values())    # dict_values([3, 3, 3])
print(my_counter.most_common(2))    #[('a', 3), ('b', 3)]
print(my_counter.most_common(1))    # [('a', 3)]
print(my_counter.most_common(1)[0][0])    # a
print(list(my_counter.elements()))  # ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']

from collections import namedtuple 
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)   #1 -4

from collections import OrderedDict 
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)     # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

from collections import defaultdict 
d = defaultdict(float)        # float
d['a'] = 1
d['b'] = 2  # 2
print(d['b'])   # 2 
print(d['c'])   # 0.0

# deque is double ended queue 
# can add / remove elements from both ends 
from collections import deque 
d = deque()
d.append(1)
d.append(2)
print(d)    #deque([1, 2])

d.appendleft(3)
print(d)

d.pop() # remove last item 
print(d)    #deque([3, 1])

d.popleft()
print(d)    #deque([1])

d.clear()   # clean dequeu
d.extend([4,5,6])
print(d)    #deque([4, 5, 6])

d.extendleft([4,5,6])     # extend to left 
d.rotate(1)  # rotate 1 place