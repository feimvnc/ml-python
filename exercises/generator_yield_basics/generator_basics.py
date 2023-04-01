'''
generator functions are a special kind of function that return a lazy iterator. 
These are objects that you can loop over like a list. 
However, unlike lists, lazy iterators do not store their contents in memory

Uses cases
'''

# uncomment below to create data.csv file 
# reading larges files , to avoid MemoryError
# create a sample csv file 
# import csv
# with open("data.csv", "w") as f:
#     writer = csv.writer(f)
#     for row in range(1000):
#         writer.writerow([row, row+1, row+2, row+3])


# generator expression , read file and print last line 
from imp import init_frozen


file_name = "data.csv"
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row 
 

gen = csv_reader(file_name)     # call function
first = last = next(gen)    # set first value
for last in gen: pass       # till the last value 
print(f"gen first: {first}")
print(f"gen last: {last}")


# generator expression , read file and print last line 
file_name = "data.csv"
csv_gen = (row for row in open(file_name))
first = last = next(csv_gen)
for last in csv_gen: pass
print(f"csv_gen {last}")


# generate an infinite sequence 
def infinite_sequence():
    num = 0 
    while True:
        yield num 
        num += 1 

# print and check infinite_sequence()
for i in infinite_sequence():
    print(i, end=" ")  # 0 1 2 3 4 5 6 7 8 9 10 
    if i == 10: # stop loop at 10 
        break


# use next to iterate from generator 
gen = infinite_sequence()
for i in range(5):
    print(next(gen))
'''
0
1
2
3
4
'''


# list vs generator
num_1 = [n**2 for n in range(5)]   # list 
num_2 = (n**2 for n in range(5))   # generator 
print(num_1)    # [0, 1, 4, 9, 16]
print(num_2)    # <generator object <genexpr> at 0x7fd878233a70>


# profile generator 
import sys 
nums_squared_lc = [ i ** 2 for i in range(10000)]   # list comprehension 
print(sys.getsizeof(nums_squared_lc))   # 85176

nums_squared_lc = ( i ** 2 for i in range(10000))   # generator 
print(sys.getsizeof(nums_squared_lc))   # 104 , size is much smaller 


# use StopIteration exception 
letters = list("hello")
print(letters)
it = iter(letters)
while True:
    try:
        letter = next(it)
    except StopIteration:   # signal end of iterator 
        break 
    print(letter)
'''
h
e
l
l
o
'''

# create data pipeline with generator 
# note: for csv files, it is recommended to use csv module in standard library 
file_name = "data.csv"
lines = (line for line in open(file_name))  #read in each line of file 
list_line = (s.rstrip().split(",") for s in lines)   # split line into values, put in a list 
cols = next(list_line)  # use next() to store the column names in a list 
data_dicts = (dict(zip(cols, data)) for data in list_line)
print(next(data_dicts))
summary = (     # this is a generator 
    int(data_dict["0"])         # get first column
    for data_dict in data_dicts
    if int(data_dict["1"]) % 5 == 0     # filter 2nd column value 
)
total_amount = sum(summary)         # summary 
print(f"Total : {total_amount}")

# Total : 100300



