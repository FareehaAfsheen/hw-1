class animal:
    def __init__(self, c):
        self.colour = c

class dog(animal):
    def __init__(self, n, c):
        super().__init__(c)
        self.name = n

class cat(animal):
    def __init__(self, n, c):
        super().__init__(c)
        self.name = n

class pet:
    def __init__(self, o):
        self.owner = o

class HybridDog(dog, pet):
    def __init__(self, n, c, o, a):
        dog.__init__(self, n, c)
        pet.__init__(self, o)
        self.age = a

    def show(self):
        print("Name:", self.name)
        print("Color:", self.colour)
        print("Owner:", self.owner)
        print("Age:", self.age)
Dog_name  = input("Enter dog name: ")
Dog_color = input("Enter dog colour: ")
Dog_owner = input("Enter owner name: ")
Dog_age   = input("Enter dog age: ")

h1 = HybridDog(Dog_name, Dog_color, Dog_owner, Dog_age)
h1.show()  