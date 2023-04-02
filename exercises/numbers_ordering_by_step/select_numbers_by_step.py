from typing import List
import numpy as np 

class Solution:
    # number_size: how many 
    # step: how to sort
    # must pass 3 total parameters: self, numbers_size, step_size

    def select_numbers_by_step(self, numbers_size: int, step_size: int) -> List:
        numbers_list = np.array(list(range(1, numbers_size)))  # create array 
        results = []   # init the list 
        start = 0 
        while len(numbers_list) > step_size: # loop through the remaining list 
            results.extend(numbers_list[::step_size])    #    append first selection to results 
            # option 1, list comprehension 
            # numbers_list = [n for n in numbers_list if n not in results]

            # option 2, use set() method, ** set() subtraction changes order, pay attention
            # numbers_list = list(set(numbers_list) - set(results)) 
            # sorted() to keep the number in order, ok in this case  
            # sorted(numbers_list)   
            # 

            # option 3, use single () method, order is kept
            # results_set = set(results)
            # numbers_list = [ n for n in numbers_list if n not in results_set]

            # option 4, use set() inside list comprehension, similar to above 
            # numbers_list = [n for n in numbers_list if n not in set(results)]

            # option 5, use set().difference 
            # numbers_list = list(set(numbers_list).difference(results))

            # option 6, use collections.Counter()
            # from collections import Counter
            # numbers_list_c = Counter(numbers_list)
            # results_c = Counter(results)
            # numbers_list = list(numbers_list_c - results_c)

            # option 7, for loop np.argwhere 
            for i in numbers_list:
                for j in results: 
                    if i == j:
                        index = np.argwhere(numbers_list==i)   # get index 
                        numbers_list = np.delete(numbers_list, index)   # delete value at index

            mylist = np.setdiff1d(numbers_list, results)

            # option 8, boolean indexing or masking, todo

        results.extend(numbers_list)   # append last remaining numbers < step 

        # option 2, 5 only, **must use sorted here also to keep in order 
        # results.extend(sorted(numbers_list))
        return results 


test = Solution()

output = test.select_numbers_by_step(21, 3)   
print(f"size: {len(output)}\noutput: {output}")

# size: 19
# output: [1, 4, 7, 10, 13, 16, 19, 2, 6, 11, 15, 3, 9, 17, 5, 14, 8, 12, 18]


# enumerate alternatives 
def remove_every_other(lst):    # use enum
    result = []
    for i, val in enumerate(lst):
        if i % 2 == 0:
            result.append(val)
    return result 

def remove_every_other_listcomp(lst):
    return [ i for i in lst if i % 2 != 0]


# much simpler form 
lst = list(range(10))
new_lst = lst[::2]    