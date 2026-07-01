class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self, hours):
        print(f"{self.name} is sleeping.")
        return hours 

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Buddy")
cat = Cat("Tom")
mouse = Mouse("Jerry")
mouse_sleep = mouse.sleep

print(dog.name)
print(dog.is_alive)
print(mouse_sleep(5))


