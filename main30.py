# IF AND ELSE SHORTHAND
# a = 303
# b = 3033
# print("A") if a > b else print("=") if a == b else print ("B") 

# ENUMURATE FUNCTION
# marks = [ 23, 40, 24, 100, 55]

# for index, mark in enumerate(marks):
#     print(mark)
#     if(index == 3):
#         print("Vansh, thats great")

fruits = ( "apple", "banana", "pears", "pappaya")
for index, fruit in enumerate(fruits, start = 1):
    print(fruit)
    if(index==2):
        print("-> ohhh yes i love ANVI'S pears")
print(type(fruits))