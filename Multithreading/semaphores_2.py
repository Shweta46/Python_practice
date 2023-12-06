from time import sleep
from random import random
from threading import Thread
from threading import Semaphore
def task(semaphore, number):
    with semaphore:
        value = random()
        sleep(value)
        print(f'Thread {number} got {value}')
semaphore = Semaphore(2)
for i in range(10):
    worker = Thread(target=task, args=(semaphore, i))
    worker.start()