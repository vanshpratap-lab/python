class employee:
    def __init__(self,name,**kwargs):
        super().__init__(**kwargs)
        self.name = name
class dancer:
    def __init__(self,dance,**kwargs):
        super().__init__(**kwargs)
        self.dance = dance

class EmployeeDancer(employee,dancer):
    def __init__(self,name,dance,level):
        super().__init__(name=name,dance=dance)
        self.level = level

    def script(self):
        print(f"name is {self.name} and he/she is a {self.dance} and is on {self.level} level")

ed = EmployeeDancer("arjav","dancer","advance")
ed.script()
print(EmployeeDancer.mro()) # used for knowing the exact order of methodss used in inehritance