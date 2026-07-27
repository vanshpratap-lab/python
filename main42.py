# OBJECTED ORIENTED PROGRAMMING
# class person:
#     name = "vansh"
#     occupation = "enterpreneur"
#     net_worth = "10 billion dollars"


# a = person ()
# b = person ()
# c = person ()
# print(a.name, a.occupation, a.net_worth)

# class person:
#     name = "vansh"
#     occ = "enterpreneur"

#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a = person ()
# a.info()
#---------------------CONSTRUCTORS---------------------- 
class person :
    def __init__(self,name,occupation,net_worth):
        self.name = name
        self.occupation = occupation 
        self.net_worth = net_worth

a = person("vansh","enterpreneur", "10 billion dollars")
b = person("anvi", "proffesor", "20 lakhs")
c = person("shreyansh", "coach", "30 lakhs")

print(f"{a.name} is a {a.occupation} and his net worth is {a.net_worth}")
print(f"{b.name} is a {b.occupation} and her net worth is {b.net_worth}")
print(f"{c.name} is a {c.occupation} and his net worth is {c.net_worth}")
