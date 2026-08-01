class person:
    def __init__(self, id, name, salary, rank):
        self.id = id
        self.name = name
        self.salary = salary
        self.rank = rank

    def show(self):
        print(f"sir {self.name} with firm id {self.id} have a net worth of {self.double_salary} billion dollars and is ranekd no. {self.rank}")
    # def show2(self):
    #     print(self.double_salary) ------> no need to use this method as it is for printing outside the main body

    @property
    def double_salary(self):
        return 10 * self.salary
a = person("10", "Vansh", 10, "1")
b = person("9", "Surya", 9, "2")

a.show()
b.show()
# a.show2() -------> prints it but gets printed again in bottom line
# b.show2() ------> same output as above 
# print(a.id, a.name , a.salary, a.rank) #------> long method 
# print(b.id, b.name, b.salary, b.rank) #-------> long method

