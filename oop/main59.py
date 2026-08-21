# import time
# print("starting")
# time.sleep(3)
# print("waited for 3 seconds")

# print(time.time())

import time
start = time.time()
time.sleep(2)
end = time.time()
print(f"took {end - start:.2f} seconds")

print(time.ctime())
