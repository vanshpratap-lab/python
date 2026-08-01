# -----------------DECORATORS-----------------
# def greet(fx):
#     def mfx():
#         print("good morning")
#         fx()
#         print("thanks for using this function")
#     return mfx

# @greet
# def hello():
#     print("hello world")

# hello()

# def x(f):
#     f()
#     f()
# def y():
#     print("hi!!")
# x(y)         

# def adder():
#     def a_adder(x):
#         return x + 10
#     return a_adder
# addition = adder()
# print(addition(20))

# Version B - using @

# def loud(x):
#     def wrapper():
#         print("starting")
#         x()
#         print("ending")
#     return wrapper
# @loud
# def say_hi():
#     print("hi!!")
# say_hi()

def adder(x):
    def wrapper(*args, **kwargs):
        print("starting")
        result = x(*args,**kwargs)
        print("ending")
        return result
    return wrapper

@adder
def add(): #<------------ dont pass arguments like (a,b) it will be empty directly give values to a and b 
    a = 20
    b = 40
    print(a+b)
add()
