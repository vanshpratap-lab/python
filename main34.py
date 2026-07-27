# LOCAL VARIBALE VS GLOBAL VARIBALE

# x = 4
# print(x)

# def hello():
#     x = 5
#     print(f"the local x is {x}")
#     print("hello vansh")

# print(f"the global x is {x}")
# hello()
# x = 5
# print(f"the global x is {x}")

x = 10

def my_function():
    global x
    x = 4
    y = 5 
    print(y)

my_function()
print(x)
# print(y) 
 