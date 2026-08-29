user_input = int(input("please enter your no."))
cache = {}
def fib(n):
    if n in cache:
        return cache[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        result =  fib(n - 1) + fib(n - 2) 
        cache[n] = result
        return result

print(fib(user_input))