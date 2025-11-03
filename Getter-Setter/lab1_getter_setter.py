# Lab 1: Person Class (Getter/Setter Validation)
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = None
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Age must be positive!")

if __name__ == "__main__":
    p = Person("John", 25)
    print(p.name, p.age)
    p.age = -5
