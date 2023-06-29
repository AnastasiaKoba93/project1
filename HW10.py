

class Car:
    def wheels(self):
        print("Number of wheels: 4")

    def mode_of_transport(self):
        print("Mode of transport: Private usage")


class Bus:
    def wheels(self):
        print("Number of wheels: 8")

    def mode_of_transport(self):
        print("Mode of transport: Public usage")


car1 = Car()
bus1 = Bus()

vehicles = [car1, bus1]

for vehicle in vehicles:
    vehicle.wheels()
    vehicle.mode_of_transport()
    print()


class Vehicle:
    def desc(self):
        pass

    def wheels(self):
        pass


class Car(Vehicle):
    def desc(self):
        print("This is a car")

    def wheels(self):
        print("Number of wheels: 4")


class Bus(Vehicle):
    def desc(self):
        print("This is a bus")

    def wheels(self):
        print("Number of wheels: 8")


car2 = Car()
bus2 = Bus()

vehicles2 = [car2, bus2]

for vehicle in vehicles2:
    vehicle.desc()
    vehicle.wheels()
    print()



class MyClass:
    def __init__(self):
        self._a = 10
        self.__a = 20

obj = MyClass()

print(obj._a)
print(obj._MyClass__a)
