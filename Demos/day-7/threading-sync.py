# semaphore object for Thread synchronization

# The basic concept of the semaphore is to use an internal counter which is decremented by each acquire() call and incremented
# by each release() call. The counter can never below zero and when acquire() finds that is zero, waiting until some threads call release(). 

# the semaphore class in threading module defines acquire() and release() methods. 
# 
# # the acquire() method 
# locks a synchronization primitive (like a mutex or lock)  to grant a thread exclusive access to a shared resource. 
# if the lock is already held by another thread, acquire() pauses the requesting thread until the lock is released. 
# 
# Release() method 
# Releasing the semaphore, increment the internal counter object by 1, when it was zero on entry and other threads are waiting for it
# become larger than zero again, wake up n of the those threads. 
# 
# Use Semaphore object in python to control access to a shared resource among multiple threads, for avoiding deadlock in multithreads. 
# 
from threading import * 
import threading
import time 

# create a thread instance where count = 3 

lock = Semaphore(4)

# creating the thread instance 
def synchorized(name):
    # calling acquire method 
    lock.acquire()

    for n in range(3):
        print('Hello', end ='')
        time.sleep(1)
        print(name)       
        
         # calling release method 
         
    lock.release()


# Create a lock object 
lock = threading.Lock()  # lock object creation
shared_counter = 0 

def increment():
    global shared_counter
    # acquire the lock before entering the OS process critical section 
    if lock.acquire():
        try:
            print(f"lock acquired by {threading.current_thread().name}")
            shared_counter += 1 # critical section of PCB 
        finally: 
            lock.release() # ensure the lock is released after the work is completed
            print(f"Lock is released by {threading.current_thread().name}")

# Create and start multiple threads 
threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    t.start()  # start the thread 
    threads.append(t)

 # wait for all threads to complete 
for t in threads:
    t.join()

print(f"Final counter value: {shared_counter}")

# non blocking acquire() method for locking the thread object 
# automatic timeout values for acquire() method while a thread tries to get the lock without waiting. 

lock = threading.Lock() # create the lock object 

# method for attempting to acquire the lock without waiting 

def try_lock(): 
    if lock.acquire(blocking=False): # attempting to acquire the lock without waiting 
        try: 
            print(f"lock acquired by {threading.current_thread().name}")
        finally: 
            lock.release()
            print(f"lock is released by {threading.current_thread().name}")   
    else:
        print(f"lock is not acquired by {threading.current_thread().name}")

# try to create the thread with range() function
threads = [threading.Thread(target=try_lock) for _ in range(3)]

for t in threads: 
    t.start()

for t in threads():
    t.join()    



# Thread lock with timeout value 

lock = threading.Lock() # create the lock object 

# method for attempting to acquire the lock without waiting 

def try_lock_with_timeout(): 
    if lock.acquire(timeout=3): # lock would be timed out after 3 sec  
        try: 
            print(f"lock acquired by {threading.current_thread().name}")
        finally: 
            lock.release()
            print(f"lock is released by {threading.current_thread().name}")   
    else:
        print(f"lock is not acquired by {threading.current_thread().name}")

# try to create the thread with range() function
threads = [threading.Thread(target=try_lock_with_timeout) for _ in range(3)]

for t in threads: 
    t.start()

for t in threads():
    t.join()    


