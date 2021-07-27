from threading import Thread
import threading


class PrintThread(Thread):
    def run(self):
        for n in range(1, 11):
            print(n)


t = PrintThread()
t.setName("Child")
t.start()
print("No. of threads : ", threading.active_count())
print(list(threading.enumerate()))