# def int(x):
    # return x*2

def appl(fx, value):
    return 6 + fx(value)

int = lambda x: x*2
cube = lambda x: x**3
avg = lambda x, y, : (x+y)/2


print(int(5))
print(cube(5))
print(avg(3,6))
print(appl(lambda x: x*x*x, 2))    