#  PROCEDURAL ORIENTED APPROACH

# marks = int(input("please enter your marks : "))

# if marks >= 85:
#     print("A+")
# elif marks >= 70:
#     print("A")
# elif marks >= 55:
#     print("B+")
# elif marks >= 40:
#     print("B")
# else :
#     print("fail")

# OBJECT ORIENTED APPROACH

# class studentmarks:
#     def __init__(self):
#         self.marks = None

#     def grade(self):
#         marks = int(input("please enter your marks : "))
#         if marks >= 85:
#             print("A+")
#         elif marks >= 70:
#             print("A")
#         elif marks >= 55:
#             print("B+")
#         elif marks >= 40:
#             print("B")
#         else :
#             print("fail")

# sm = studentmarks()
# sm.grade()


# OTHER WAY 
class studentmarks:
    def __init__(self,marks):
        self.marks = marks

    def grade(self):
        if self.marks >= 85:
            print("A+")
        elif self.marks >= 70:
            print("A")
        elif self.marks >= 55:
            print("B+")
        elif self.marks >= 40:
            print("B")
        else :
            print("fail")
user_input = int(input("please enter your marks : "))
sm = studentmarks(user_input)
sm.grade()