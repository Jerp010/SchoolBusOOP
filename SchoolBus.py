from abc import ABC, abstractmethod

# Abstraction: Abstract Base Class
class Vehicle(ABC):
    def __init__(self, brand, wheels):
        self._brand = brand  # Protected attribute (Encapsulation)
        self._wheels = wheels

    def get_brand(self):
        return self._brand

    @classmethod
    def vehicle_info(cls):
        print("Vehicles are machines used for transportation.") #For using class methods

# Inheritance: SchoolBus inherits from Vehicle
class SchoolBus(Vehicle):
    def __init__(self, brand, wheels, capacity):
        super().__init__(brand, wheels)
        self.__capacity = capacity  # Private attribute (Encapsulation)

    def get_capacity(self):
        return self.__capacity


# Outputs
def main():
    bus = SchoolBus("Mercedes", 6, 50)

    # Encapsulation via getters
    print("Brand:", bus.get_brand())
    print("Capacity:", bus.get_capacity())

    # Calling Class Method
    Vehicle.vehicle_info()

    # Inheritance check
    print("Is 'bus' an instance of Vehicle?", isinstance(bus, Vehicle)) #Checks with built it function

if __name__ == "__main__":
    main()
