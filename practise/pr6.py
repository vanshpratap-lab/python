import time
numbers = []

for num in range(5):
    user_input = int(input("please enter your numbers : "))
    numbers.append(user_input)
print(numbers)
time.sleep(2)
avg = sum(numbers) / len(numbers)
print(f"the avergae is : {avg}")