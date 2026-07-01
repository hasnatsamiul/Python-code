class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def Drive(self):
        print(f"You drive the {self.model}")

    def Stop(self):
        print(f"The {self.model} has stopped")