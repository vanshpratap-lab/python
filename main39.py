def cube(x):
    return x**3

print(cube(2))

l = [1,2,3,4,5,6]
newl = list(map(cube, l))
print(newl)