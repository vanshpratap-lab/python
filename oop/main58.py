# ----------Hierarchical inheritance----------

class species:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def script1(self):
        print(f"a specie have a {self.name} and  live {self.age}")

class human(species):
    def __init__(self, name, age, language, walklegs):
        super().__init__(name, age)
        self.language = language
        self.walklegs = walklegs

    def script2(self):
        print(f"there are {self.name} and live {self.age} and speaks {self.language} and walks on {self.walklegs}")

class animal(species):
    def __init__(self, name, age, language, walklegs):
        super().__init__(name, age)
        self.language = language
        self.walklegs = walklegs

    def script3(self):
        print(f"{self.name} have {self.age} and speaks {self.language} and walks on {self.walklegs}")

class cat(animal):
    def __init__(self, name, age, language, walklegs):
       super().__init__(name, age, language, walklegs)

    def script4(self):
        print(f"{self.name} is of {self.age} and speaks {self.language} and walks on {self.walklegs}")

class dog(animal):
    def __init__(self, name, age, language, walklegs, dog_species):
        super().__init__(name, age, language, walklegs)
        self.dog_species = dog_species

    def script5(self):
        print(f"{self.name} is of {self.age} and speaks {self.language} and walks on {self.walklegs}")

class bigcat(cat):
    def __init__(self, name, age, language, walklegs):
        super().__init__(name, age, language, walklegs)

    def script6(self):
        print(f"big cats are {self.name}")

sp = species("humans", "upto 100 years")
sp.script1()

hm = human("humans", "upto 100", "understandable language", "2 legs")
hm.script2()

am = animal("animals", "upto 80 years", "animals language", "4 legs")
am.script3()

ct = cat("cat", "upto 18 years", "meow", "4 legs")
ct.script4()

dg = dog("dog", "upto 14 years", "bark", "4 legs", "Canine")
dg.script5()

bc = bigcat("lion", "upto 14 years", "roar", "4 legs")
bc.script6()
