# Lab 1: Rectangle Class
# -----------------------
# Yêu cầu:
# 1. Tạo class Rectangle có fields: width, height
# 2. Viết hàm tính diện tích (area) và chu vi (perimeter)
# 3. Tạo đối tượng để kiểm tra kết quả

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Test
if __name__ == "__main__":
    r = Rectangle(5, 3)
    print("area:", r.area())
    print("Perimeter:", r.perimeter())
