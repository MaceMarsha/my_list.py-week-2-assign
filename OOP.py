# Activity 1: Superhero class with inheritance

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name} from {self.city}, and my power is {self.power}!")

    def save_the_day(self):
        print(f"{self.name} saves the day using {self.power}!")

# Inheritance: Sidekick class
class Sidekick(Superhero):
    def __init__(self, name, power, city, hero_name):
        super().__init__(name, power, city)
        self.hero_name = hero_name

    def assist(self):
        print(f"{self.name} assists {self.hero_name} with {self.power}!")

# Example usage
hero = Superhero("Captain Code", "Bug Fixing", "PyCity")
sidekick = Sidekick("Debug Boy", "Log Reading", "PyCity", "Captain Code")

hero.introduce()
hero.save_the_day()
sidekick.introduce()
sidekick.assist()

print("\n--- Polymorphism Challenge ---\n")

# Activity 2: Polymorphism with vehicles

class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Example usage
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()