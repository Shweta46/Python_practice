# importing thread module
import threading

def print_cube(num):
    print("Cube: {}".format(num*num*num))

def print_square(num):
    print("Square: {}".format(num*num))

if __name__ == "__main__":
    # to create a thread
    t1 = threading.Thread(target=print_cube,args=(10,))
    t2 = threading.Thread(target=print_square, args=(10,))

    # to start a thread
    t1.start()
    t2.start()

    # ending a thread execution
    t1.join()
    t2.join()

    # As a result, the current program will first wait for the completion of t1 and then t2.
    # Once, they are finished, the remaining statements of the current program are executed.
    print("Done!")

