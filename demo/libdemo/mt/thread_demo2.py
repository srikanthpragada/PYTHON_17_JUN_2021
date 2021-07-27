from threading import Thread
import threading


def print_numbers():
    for n in range(1, 11):
        print(n)


t = Thread(target=print_numbers)
t.setName("Child1")
t.start()

t2 = Thread(target=print_numbers)
t2.setName("Child2")
t2.start()

print("No. of threads : ", threading.active_count())
print(list(threading.enumerate()))
