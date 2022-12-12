# start 11 thread within 1 process 
# 1 main + 11 child threads 
# threads run in same process space, which can access shared memory data 

from threading import Thread 
import os 
import time 

def square_numbers():
    for i in range(2):
        i * i 
        time.sleep(0.5)

threads = []
num_threads = 10

def main():
    # create processes 
    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t) 
        # print(processes.index)

    # start 
    for p in threads:
        p.start()
        print("starting...")

    # join , here block main process 
    for t in threads:
        t.join()    # wait and block the main thread until thread completes 

    print('end main')
 
if __name__ == "__main__": 
    main()