import threading
import time

def loop_one():
    while True:
        print("Loop One is running...")
         # Simulate some work

def loop_two():
    while True:
        print("Loop Two is running...")
         # Simulate some work

def loop_3():
    while True:
        print("Loop 3 is running...")
         # Simulate some work

def loop_4():
    while True:
        print("Loop 4 is running...")
         # Simulate some work
# Create thread objects
thread1 = threading.Thread(target=loop_one)
thread2 = threading.Thread(target=loop_two)
thread3 = threading.Thread(target=loop_3)
thread4 = threading.Thread(target=loop_4)

# Start the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()