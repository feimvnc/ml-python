from multiprocessing import Pool

def cube(number):
    return number * number * number 

if __name__ == "__main__":
    numbers = range(10)
    pool = Pool()
    # map, apply, join, close - 4 Pool methods 
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])  # with one argument 
    pool.close()
    pool.join()

    print(result)  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
