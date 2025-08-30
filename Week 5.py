# =============================
# Assignment 1: Smartphone Class
# =============================

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        # Attributes
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    # Method: display phone details
    def phone_info(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}mAh"

    # Method: simulate charging
    def charge(self, amount):
        self.battery += amount
        return f"{self.model} charged! Battery now {self.battery}mAh"

# Inheritance Example
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    # Method specific to GamingPhone
    def game_mode(self):
        return f"{self.model} is now in Game Mode with {self.cooling_system} cooling system!"

# Create objects
phone1 = Smartphone("Apple", "iPhone 15", 256, 3200)
phone2 = GamingPhone("Asus", "ROG 7", 512, 6000, "liquid-cooling")

# Demonstration
print(phone1.phone_info())
print(phone2.phone_info())
print(phone2.game_mode())
print(phone1.charge(300))

# =============================
# Activity 2: Polymorphism
# =============================

class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
