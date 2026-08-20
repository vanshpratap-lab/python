class operator:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return (f"{self.i}i + {self.j}j + {self.k}k")

v1 = operator(1,2,3)
# print(v1)

        

