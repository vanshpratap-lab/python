# -------Walrus operetor--------
# list = [1,2,3,4,5]

# while (n := len(list)) > 0 :
#     print(list.pop())

foods = list()
while True :
    food = input("what food do you like? : ")
    if food == "quit":
        break
    foods.append(food)
print(f"your foods : {foods}")