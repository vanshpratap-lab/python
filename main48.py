# Instance variables and Class variables 
# class person:
#     count = 0 

#     def __init_(self,name):
#         self.name = name
#         person.count += 1

# a = person("vansh")
# b = person("shreyansh")
# c = person("arjav")

# print(a.name,b.name,c.name)
# print(person.count)

class Car:
    wheels = 4

    def __init__(self,name):
        self.name = name

car1 = Car("rolls royce")
car2 = Car("bentley")

car1.wheels = 6

print(car1.wheels)
print(car2.wheels)
print(Car.wheels)