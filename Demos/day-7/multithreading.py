# multithreading in python allows multiple threads to execute concurrently. Enabling efficient multitasking. 

# it's useful for I/O bound tasks like network request, file transfer, user interactions. 
# A process can have multiple threads
# Threads share the same code and global data structure which have their own registers and local variables(stack)
# Thread is a lightweight process. 
# a multihreaded [process] can run multiple tasks in parallel by having seperate stacks/registers for each thread, but sharing 
# the same code and data.

import threading
import time 

def square(num):
    print(f"square of numbers: {num*num}")
    time.sleep(1)

def cube(num):
    print(f"cube of numbers: {num*num*num}")
    time.sleep(1)

# thread execution
t1 = threading.Thread(target=square, args=(4,))
t2 = threading.Thread(target=cube, args=(7,))  

# start the thread
t1.start()
t2.start()

# join the thread
t1.join()
t2.join()

print("Multithreading example in Python!")

# Daemon threads -> they run in background and are automatically killed when the main program exits. They are
# ideal for background services like logging, monitoring. 

# use daemon=True to create the daemon thread

import threading, time 

def background():
    while True:
        print("Daemon thread is running...")
        time.sleep(1)

t = threading.Thread(target=background, daemon=True)
t.start()
time.sleep(3)
print("Main thread exiting; daemon thread killed automatically")     

# In multithreading, threads often need to share data (like variables, files, lists, database/network connections)
# multiple threads might try to modify the same resource at the same time. 

# a race condition happens when the final result depends on unpredictable timing of threads 
# to prevent this, the threading module in python provides the synchoronization primitives. These are special objects 
# which co-ordinates thread across the shared resources. 

import threading 

counter = 0 
lock = threading.Lock()   # creates a mutual exclusion object 

# method increment 

def increment():
    global counter 
    for _ in range(100000):
        with lock:  # prevents the race condition (OS deadlock)
            counter += 1

# creating 6 threads and starting them
threads = [threading.Thread(target=increment) for _ in range(5)]
[t.start() for t in threads]
[t.join() for t in threads]

print("Final Counter value: ", counter)

# Thread communication 

# An event in thread is like flag that one thread sets, and other threads wait for. 
# It is useful when one thread must wait for a signal before continuing (like waiting for task to complete)

import threading , time 

event = threading.Event()  # event object 

def waiter():
    print("thread is waiting for the event")
    event.wait() # blocks until the event.set() is called 
    event.clear() # continue blocking 
    print("Thread got the event signal! continuing work")
    

t = threading.Thread(target=waiter)
t.start()

time.sleep(4) # simulate some work 
print("Main thread is sending signals....")
event.set()  # signal the waiting thread to resume the operation
 # reset the flag to false. threads calling the wait method after this will block until is set is called again


