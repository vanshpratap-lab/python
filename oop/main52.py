class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

a = person("vansh","19")
print(a.name,a.age)
print(dir(a))
print(a.__dict__)
print(help(person))