class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"mark: {self.make}, model: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        Vehicle.__init__(self, make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = Vehicle.get_info(self)
        return f"{base_info}, Fuel Type: {self.fuel_type}"  

vehicle = Vehicle("Toyota", "Camry")
print(vehicle.get_info())

car = Car("Honda", "Civic", "Gasoline")
print(car.get_info())