class Elevator:
    def __init__(self, starting_floor):
        self.make = "The elevator company"
        self.floor = starting_floor

# To create the object

elevator = Elevator(45)
print(elevator.make) # "The Elevator company"
print(elevator.floor) # 1

class Car:
    def __init__(self, color, make):
        self.color = color # ends up on the object
        self.make = make # becomes a local variable in the constructor

car = Car("Red", "Ferrari")
print(car.color) # "Red"
print(car.make) # would result in an error, `make` does not exist on the object