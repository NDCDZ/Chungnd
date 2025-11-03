# Lab 3: Laptop Class (Validated Getter/Setter)
class Laptop:
    def __init__(self, brand, price):
        self._brand = None
        self._price = None
        self.brand = brand
        self.price = price

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if value.strip():
            self._brand = value
        else:
            print("Brand cannot be empty!")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Price must be greater than 0!")

if __name__ == "__main__":
    l = Laptop("Dell", 1200)
    print(l.brand, l.price)
    l.price = -100
    l.brand = ""
