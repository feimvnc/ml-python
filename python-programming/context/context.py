# context helps to manage resources 
# close resources, connections 

# typical way to open file using context manager , and free resources
with open('hello.txt', 'w') as file:
    file.write('world ...')

# normal way to open file using checks to close 
file = open('notes.txt', 'w')
try:
    file.write('world...')
finally:
    file.close()

# free lock 
from threading import Lock 
lock = Lock()

# normal way, bad 
lock.acquire()
# do task 
lock.release()

# better way, resources freed up automatically 
with lock:
    #...

## for class, use __enter__ and __exit__ methods 
class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename 
    
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file 

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exc', exc_type, exc_value)
        print('exit')
        return True 

# init, enter, exit methods are called automatically 
with ManagedFile('hello.txt') as file:
    print('start...')
    file.write('hello_word...')
print('continuing...')


## function annotation 
from contextlib import contextmanager 

@contextmanager 
def open_managed_file(file):
    f = open(filename, 'w')
    try: 
        yield f
    finally: 
        f.close()

with open_managed_file('hello.txt') as f:
    f.write('to do task ...')
