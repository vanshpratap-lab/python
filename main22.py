# def square(n):
#     '''takes in a number n , return the square of n'''
#     print(n**2)
# square(5)
# print(square.__doc__
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
print(factorial(4))
print(factorial(3))
