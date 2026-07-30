# ----------INHERITANCE----------
class pen:
    def __init__(self, shape, length, width):
        self.shape = shape 
        self.length = length
        self.width = width

    def show(self):
        print(self.shape, self.length, self.width,)


class pen2(pen):
    def __init__(self, shape, length, width, radius):
        super().__init__(shape,length,width)
        self.radius = radius
    

    def show(self):
        super().show()
        print(self.radius)

# a = pen("cylinder","12cm","1cm")
# a.show()
a = pen2("cylinder","12cm","1cm","0.5cm")
a.show()
