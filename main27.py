# EXCEPTION HANDLING 
# a = (input("enter the number :"))
# print(f"multiplication of {a} is:")
# try :
#     for i in range (1,11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
# except Exception as e :
#     print("invalid input!")

# print("some imp lines of codes")
# print("end of program") 

try: 
    num = int(input("enter your value:"))
    a = (5,3)
    print(a[num])
    # print(f"{num*2}") 
except ValueError:
    print("number entered is not and integer")
except IndexError:
    print("index error")
