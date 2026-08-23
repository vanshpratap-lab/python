# -------Generators--------
# used for using less memory it is used to create on fly values means in a list a memory is created and then the vales are itereated but by generators we create memory and iterate at the same time and it continues 
# def get_square(n):
#     result = []
#     for i in range(n):
#         result.append(i * i)
#         return result
# squares = get_square(10)

def generator():
    for i in range(10):
        yield i

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))