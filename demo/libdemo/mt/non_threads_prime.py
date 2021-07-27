import math
from threading import Thread
import threading
from datetime import datetime


def isprime(num):
    for n in range(2, math.floor(math.sqrt(num)) + 1):
        if num % n == 0:
            print(f"{num} is not a prime number!")
            break
    else:
        print(f"{num} is a prime number!")


starttime = datetime.now()
nums = [393939393, 12121212121, 29292939327, 38433828281, 62551414124111]
for n in nums:
    isprime(n)

endtime = datetime.now()
diff = (endtime - starttime).microseconds
print("No. of Microseconds taken : ", diff)
