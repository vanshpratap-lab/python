# -------multithreading module------------
# multithreading module is usedlike when you wanna downlaod things parallely togetehr rather then one by one to exefute tasks togetehr ratehr then oneby one you use mulithreading

import threading 
import time

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

func(4)
func(2)
func(1)

time1 = time.perf_counter()

t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

time2 = time.perf_counter()

print(time2 - time1)

t1.start()
t2.start()
t3.start()