from abc import ABC, abstractmethod

# Abstraction: Abstract Base Class
class Vehicle(ABC):
    def __init__(self, brand, wheels):
        self._brand = brand  # Protected attribute (Encapsulation)
        self._wheels = wheels

    @abstractmethod
    def drive(self):  # Abstract method
        pass

    def get_brand(self):  # Instance method
        return self._brand

    @classmethod
    def vehicle_info(cls):  # Class method
        print("Vehicles are machines used for transportation.")

# Inheritance: SchoolBus inherits from Vehicle
class SchoolBus(Vehicle):
    def __init__(self, brand, wheels, capacity):
        super().__init__(brand, wheels)
        self.__capacity = capacity  # Private attribute (Encapsulation)

    def drive(self):
        print(f"{self._brand} school bus is driving students to school.")

    def get_capacity(self):
        return self.__capacity


# Outputs
def main():
    bus = SchoolBus("Mercedes", 6, 50)

    # Polymorphic behavior
    bus.drive()

    # Encapsulation via getters
    print("Brand:", bus.get_brand())
    print("Capacity:", bus.get_capacity())

    # Class method
    Vehicle.vehicle_info()

    # Static method
    print("General Vehicle Usage:", Vehicle.general_usage())

    # Inheritance check
    print("Is 'bus' an instance of Vehicle?", isinstance(bus, Vehicle))


if __name__ == "__main__":
    main()
