class Car:
    def __init__(self, make, model, year): 
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        return(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
my_car = Car("Toyota", "Camry", 2020)
print(my_car.display_info())