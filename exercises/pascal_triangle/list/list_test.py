
# note: list.sort() modifies the list in-place, returns None 

list = [1,4,5,3,2]
print(list)

# sort list 
list.sort()
print(list)

# reverse sort 
list = [1,4,3,2]
list.sort(reverse=True)
print(list)
print("\r")

# sort in reverse order 
list.sort(reverse=True)
print(list)
print("\r")

# sort by key 
list = [('z',26),('a', 1), ('o', 15)]
list.sort(key=lambda x: x[0])
print(list)
print("\r")

# reverse list 
list = [3,2,5,1]
list.reverse()
print(list)       

# print item index 
list = ['a', 'z', 'b']
print(list.index('z'))

# sum list 
list = [1,2,3]
print(sum(list))
# copy list 
list = [1,2,3,4,5]
list2 = list[:]
print(list2)

# join list 
list = ['a', 'b', 'c', 'd']
list_csv = ",".join(list) 
print(list_csv)

# sort by key in reverse order 
list = [('z', 26), ('a', 1), ('o', 15)]
list.sort(key=lambda x: x[1], reverse=True)
list 
print("\r")

# sort dictionary 
# sorted() function allows you to display your list in a particular order 
# without affecting the actual order of the list 
list = [{"name": "jill", "age": 10}, 
        {"name": "joe", "age": 8}, 
        {"name": "john", "age": 10}]
list
print(sorted(list, key=lambda i: i['age']))
print("\r")
# sort by name and age 
print(sorted(list, key=lambda i: (i['age'], i['name']), reverse=True))


# list remove duplicates
list = [1,2,3,4,2]
unique_list = []
for elem in list: 
    if elem not in unique_list:
        unique_list.append(elem)
print(unique_list)

# list comprehension 
squares = []
for value in range(1,5):
    square = value**2
    squares.append(square)
print(squares)
