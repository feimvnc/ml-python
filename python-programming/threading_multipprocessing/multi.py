from multiprocessing import Process 
import os 
import time 

def square_numbers():
    for i in range(2):
        i * i 
        time.sleep(0.5)

processes = []
num_processes = os.cpu_count()

def main():
    # create processes 
    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p) 
        # print(processes.index)

    # start 
    for p in processes:
        p.start()
        print("starting...")

    # join , here block main process 
    for p in processes:
        p.join()

    print('end main')

if __name__ == "__main__": 
    main()