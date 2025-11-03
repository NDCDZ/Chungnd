# Lab 1: Tạo class Counter có biến static count. Mỗi khi tạo object mới, biến count tăng lên. In ra tổng số đối tượng đã tạo.
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

if __name__ == "__main__":
    a = Counter()
    b = Counter()
    c = Counter()
    print("Total objects created:", Counter.count)
