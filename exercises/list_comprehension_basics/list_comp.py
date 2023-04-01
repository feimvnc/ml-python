'''
list comprehensions 
fast for loops 
simplified conditional statements 
string manipulation

syntax [expression for item in list]

list comprehension vs lambda function
list comprehension is more human-readable 
'''

# use lambda inside list 
letters = list(map(lambda l: l, 'hello'))
print(letters)      # ['h', 'e', 'l', 'l', 'o']


# conditions in list comprehension 
even_list = [ i for i in range(10) if i %2 == 0]
print(f"even_list: {even_list}")
# even_list: [0, 2, 4, 6, 8]
 

# nested if in list comprehension 
filtered_list = [ i for i in range(50) \
                if i % 2 == 0 
                if i % 5 == 0
                ]
print(f"filtered_list: {filtered_list}")
# filtered_list: [0, 10, 20, 30, 40]


# if...else in list comprehension 
even_odd_list = ["even" if i%2 == 0 else "odd" for i in range(10)]
print(f"list: {even_odd_list}")
# list: ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']


# use nested loops for matrix transpose 
transposed_matrix = []
matrix = [[1,2,3,4], [5,6,7,8]]
for i in range (len(matrix[0])):  # column value
    print(i, len(matrix[0]))
    transposed_row = [] 
    for row in matrix:      # row value 
        transposed_row.append(row[i])   # each column, all row values
    transposed_matrix.append(transposed_row)
print(f"transposed_matrix {transposed_matrix}") 
# 0 4
# 1 4
# 2 4
# 3 4


# find transpose of a matrix using list comprehension 
matrix = [[1,2],[3,4],[5,6],[7,8]]
# read row[i] for all row i, loop 2 times
transpose_matrix = [[row[i] for row in matrix] for i in range(2)]
print(f"transpose_matrix: {transpose_matrix}")
# transpose_matrix: [[1, 3, 5, 7], [2, 4, 6, 8]]


# reverse each string in a tuple 
reversed_list = [string[::-1] for string in ("hello", "python")]
print(f"reversed_list: {reversed_list}")
# reversed_list: ['olleh', 'nohtyp']


# basic list iteration 
l1 = list(range(10))
for i in l1: 
    print(i)
'''
0
1
2
...
'''

# use list comprehension 
l2 = [i for i in l1]
print(l2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 

# condition statement 
x = [True, False, True, False, True]
y = []
for b in x:
    if b: 
        y.append(1)
    else:
        y.append(0)
print(x)
print(y)        
# [True, False, True, False, True]
# [1, 0, 1, 0, 1]


# use list comprehension 
z = [ 1 if b == True else 0 for b in x]
print(z)
# [1, 0, 1, 0, 1]


# string manipulation 
s = "HelloWorld"
s = [ i for i in s]   
print(s)
# ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']


# join method is often used when using string comprehension 
s = "".join([i for i in s])
print(s)   #  HelloWorld


# add space in front of each capital letter
s = "".join(
    [ i if i.islower() 
    else " " + i.lower() if i in ['W']   # change W to w, acion _ codition
    else " " + i for i in s]    # 
)[1:]  # [1: ] , remove first empty space
print(s)   #  Hello World

#
list_a = [1, 2, 3]
list_b = [item for item in list_a]     # [1, 2, 3]
list_c = [item + 1 for item in list_a] # [2, 3, 4]
list_d = [None for item in list_a]     # [None, None, None]

