class Enterpreneuer :
    company = "apple"
    def show(self):
        print(f"the name is {self.name} and the company is {self.company}")

    @classmethod
    def changeCompany(cls,newCompany):
        cls.company = newCompany

e1 = Enterpreneuer()
e1.name = "vansh"
e1.show()
e1.changeCompany("tesla")
e1.show()
print(Enterpreneuer.company)