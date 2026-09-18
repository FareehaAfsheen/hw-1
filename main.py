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
