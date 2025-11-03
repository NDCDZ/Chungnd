# Lab 2: Temperature Class
# -----------------------
# Yêu cầu:
# 1. Tạo class Temperature có method chuyển đổi giữa Celsius và Fahrenheit
# 2. Cung cấp 2 method: to_fahrenheit và to_celsius

class Temperature:
    def __init__(self, value, unit="C"):
        self.value = value
        self.unit = unit

    def to_fahrenheit(self):
        if self.unit == "C":
            return (self.value * 9/5) + 32
        return self.value  # đã là Fahrenheit

    def to_celsius(self):
        if self.unit == "F":
            return (self.value - 32) * 5/9
        return self.value  # đã là Celsius

# Test
if __name__ == "__main__":
    t1 = Temperature(25, "C")
    t2 = Temperature(77, "F")
    print("25°C =", t1.to_fahrenheit(), "°F")
    print("77°F =", t2.to_celsius(), "°C")
