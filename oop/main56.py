# ---------multilevel inhertiance and method overloading--------

class dog:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} makes sound of {self.sound}")

class animal(dog):
    def __init__(self,name,sound,country):
        super().__init__(name,sound)
        self.country = country
    def make_sound(self):
        print(f"{self.name} makes sound of {self.sound} and comes from {self.country}")

class cat(animal):
    def __init__(self,name,sound,country,size):
        super().__init__(name,sound,country)
        self.size = size

    def make_sound(self):
        print(f"{self.name} makes sound of {self.sound} and comes from {self.country} and is {self.size}")

dg = dog("labrador","bark")
dg.make_sound()

dg2 = animal("doberman","bark","argentina")
dg2.make_sound()

ct = cat("cat","meow","persian","small")
ct.make_sound()