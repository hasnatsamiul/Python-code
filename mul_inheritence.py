class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"The {self.name} is eating.")

    def sleep(self):
        print(f"The {self.name} is sleeping.")

class Prey(Animal):
    def flee(self):
        print(f"The {self.name} is fleeing.")

class Predator(Animal):
    def hunt(self):
        print(f"The {self.name} is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bunny") 

hawk = Hawk("Hawky")
fish = Fish("Nemo")


fish.flee()