# Lab 1: Counter Class (Static Variable)
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

if __name__ == "__main__":
    a = Counter()
    b = Counter()
    c = Counter()
    print("Total objects created:", Counter.count)
