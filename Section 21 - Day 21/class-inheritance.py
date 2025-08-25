# Inheritance

class Animal:
    def __init__(self, name):
        self.num_eyes = 2
        self.name = name  # store name

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)  # pass name to base class

    def breathe(self):
        super().breathe()      # call Animal's breathe
        print("Doing this underwater.")

    def swim(self):
        print(f"{self.name} is swimming")

# Create instance
nemo = Fish("Nemo")
nemo.swim()          # Nemo is swimming
nemo.breathe()       # Inhale, exhale. Doing this underwater.
print(nemo.num_eyes) # 2