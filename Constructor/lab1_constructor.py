# Lab 1: Car Class (Constructor)
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        print(f"Car created: {self.brand} {self.model} ({self.year})")

if __name__ == "__main__":
    car = Car("Toyota", "chung", 2023)
