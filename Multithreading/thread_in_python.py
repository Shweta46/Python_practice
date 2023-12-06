import threading

def say_hello(subject):
  print(f'Hello, {subject}!')

hello_thread = threading.Thread(target=say_hello, args=("World",))
hello_thread.start()
