# -------DUNDER METHODS-------

class Employee:
    def __init__(self,name,age,proffesion):
        self.name = name
        self.age = age
        self.proffesion = proffesion

    # def show(self):
    #     print(f"i am {self.name} and my age is {self.age} and i am a {self.proffesion}")

    def __len__(self):
        i = 0
        for i in self.name:
            i = i + 1
        return i 
    # def __str__(self):
    #     return f"i am {self.name} and my age is {self.age} and i am a {self.proffesion}"
    def __call__(self):
        print(f"{self.name},{self.age},{self.proffesion}")

e = Employee("umang","18","student")
# print(e)
e()
# e = Employee("umang","18","student")
# print(len(e.name))
# print(len(e.age))
# print(len(e.proffesion))
# e.show()
# print(f"{e.name},{e.age},{e.proffesion}")