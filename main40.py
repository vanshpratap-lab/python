# MAP 
# def cube(x):
#     return x*x*x
# user_input = int(input("please enter your number"))
# print(cube(user_input))
# print(cube(2))

# l = [1,2,3,4,5,6]
# newl = []
# for item in l:
#     newl.append(cube(item))
# newl = list(map(lambda x: x*x*x,l))
# print(newl)
# FILTER 
# def filter_function(a):
#     return a>2
# newnewl = list(filter(filter_function, l))
# print(newnewl)
# REDUCE
from functools import reduce
numbers = [1,2,3,4,5]

def mysum(x,y):
    return x + y
sum = reduce(mysum, numbers)
print(sum)
