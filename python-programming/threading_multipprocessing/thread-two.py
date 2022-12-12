from threading import Thread, Lock 
import time 

database_value = 0 

def increase(lock):
    global database_value 
    lock.acquire()
    local_copy = database_value 
    #processing 
    local_copy += 1 
    time.sleep(0.1)
    database_value = local_copy 
    lock.release()
    # use context manager also works , no need lock.release()
    # with lock: 
        # local_copy = database_value 
        # local_copy += 1 
        # time.sleep(0.5)
        # database_value = local_copy
    
if __name__ == "__main__":
    lock = Lock() 
    print('start value', database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)
    print('end main')


# first run value not changed to 2 
# due to race condition 
# start value 0
# end value 1
# end main

# run with Lock(), value updated correctly 
# start value 0
# end value 2
# end main
