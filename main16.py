# def average(a=5,b=6):
#     print("the average is ", (a+b)/2)
    
# average(1,5)

# def name(fname,mname="felix anthony",lname="cena"):
#     print("hello",fname,mname,lname)

# name("jhon","singh","chauhan")

# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
# #         print("the average is: ", sum/len(numbers))
#     return sum / len(numbers)

# c = average(5,6,8,3)
# print(c)

def name(**name):
    print(type(name))
    print("hello",name["fname"], name["mname"], name["lname"])
name(fname="charizard", mname="singh", lname="patel")