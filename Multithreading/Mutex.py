import time
from threading import Thread
from threading import Lock

def myfunc(i, mutex):
    mutex.acquire(1)
    time.sleep(1)
    print("Thread:", i)
    mutex.release()

def method_1():
    print("Method 1:")
    mutex = Lock()
    for i in range(0,10):
        t = Thread(target=myfunc, args=(i,mutex))
        t.start()
        print("main loop", i)


def method_2():
    print("Method 2:")
    mutex = Lock()
    for i in range(0,10):
        t = Thread(myfunc(i, mutex))
        t.start()
        print("main loop", i)

print("Both the methods will print the output differently:")
method_1()
# method_2()