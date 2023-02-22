def fibonacci_memo(n, lookup_map):
    if n <= 0:
        raise ValueError("n must be >=0")

    # memoization: check if there is a suitable pre-calculated result 
    if n in lookup_map:
        return lookup_map.get(n)

    # normal algorithm with helper variable for storing the result 
    result = 0
    if n ==1 or n == 2:
        # recursive termination 
        result = 1
    else:
        # recursive descent 
        result = fibonacci_memo(n-1, lookup_map) + fibonacci_memo(n-2, lookup_map)
    # memoization: store calculated result 
    lookup_map[n] = result 
    return result 

lm = {}
print(fibonacci_memo(20, lm))

