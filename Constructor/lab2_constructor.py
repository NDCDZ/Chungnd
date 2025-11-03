# Lab 2: User Class (Multiple Constructors)
class User:
    def __init__(self, name=None, age=None):
        self.name = name or "Guest"
        self.age = age or 0

    def __repr__(self):
        return f"{self.name} ({self.age})"

if __name__ == "__main__":
    users = [User(), User("chung", 21), User("lan", 30)]
    print("User list:", users)
