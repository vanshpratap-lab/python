# NORMAL

for i in range(20):
    if i % 3 == 0 and i % 5 == 0 :
        print(i)

# ANOTHER WAY

numbers = list(range(50))

for num in numbers:
    if not (num % 3 == 0 and num % 5 == 0):
        continue
    print(num)