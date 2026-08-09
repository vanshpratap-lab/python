class Employee:
    def __init__(self,name,occupation,salary):
        self.name = name
        self.occupation = occupation
        self.salary = salary

    @classmethod
    def fromstr(cls,string):
        return cls(string.split(",")[0],string.split(",")[1],int(string.split(",")[2]))

# e1 = Employee("umang", 40000)
# print(e1.name)
# print(e1.salary)
string = "priya,teacher,29"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.occupation)
print(e2.salary)
# -------------------------CALLING STRING METHODS WITH ANOTHER WAY------------------------------
class Employee:
    def __init__(self,name,salary,job):
        self.name = name 
        self.salary = salary 
        self.job = job
    @classmethod 
    def fromstr(cls,string):
        parts = string.split(",")
        name = parts[0]
        occupation = parts[1]
        salary = int(parts[2])
        return cls(name,occupation,salary)
string = "umang,employee,40000"
e = Employee.fromstr(string)
print(e.name)
print(e.job)
print(e.salary)