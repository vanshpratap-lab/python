class myClass:
    def __init__(self,value):
        self._value = value 

    def show(self):
        print(f"value is {self._value}")

    @property 
    def ten_value(self):
        return 10 *self._value
        
obj = myClass(10)
# obj.ten_value = 67
print(obj.ten_value)
obj.show() 