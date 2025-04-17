class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def car_info(self):
        return f"{self.brand} ,  {self.model} , {self.year}"

car = Car("BMW", "E36" , 1990)
car.car_info()
print(car.car_info())