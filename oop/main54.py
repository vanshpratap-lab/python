class Shape:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def area(self):
        return self.x * self.y # cannot do print() when method overwritting 

class circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
         return 3.14 * (self.radius**2)

c = circle(5)
print(c.area())
rec = Shape(3,4)
print(rec.area())