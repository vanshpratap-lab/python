# COUSTOM ERRORS
# a = int(input("enter any value between 5 and 9:"))

# if(a<5 or a>9):
    # raise ValueError("value should be between 5 and 9")

a = input("enter your string:")

if(a != "quit"):
    raise SystemError("string isnt correct")
else:
    print("systeam has been quit")
    