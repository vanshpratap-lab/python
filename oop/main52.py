# USING OF DIR() AND __DICT__ AND MAP() FOR INTEROSPECTION

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

a = person("vansh","19")
print(a.name,a.age)
print(dir(a))
print(a.__dict__)
print(help(person))


# USING SUPER() KEYWORD

# class Employee:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age

# class Student(Employee):
#     def __init__(self,name,age,language):
#         super().__init__(name,age)
#         self.language = language

# a = Employee("umang","18")
# print(a.name)
# print(a.age)
# b = Student("umang","18","python")
# print(b.name)
# print(b.age)
# print(b.language)


# a = Employee("umang","18")
# a()
# b = Student("umang","18","python")
# b()
