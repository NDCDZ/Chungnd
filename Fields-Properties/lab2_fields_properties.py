# Lab 2: Employee Class
# -----------------------
# Yêu cầu:
# 1. Thiết kế class Employee có các thuộc tính: name, salary, department
# 2. Tính tổng lương theo phòng ban (group theo department)
# 3. In kết quả

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

# Danh sách nhân viên mẫu
employees = [
    Employee("Chung", 1000, "IT"),
    Employee("Hải", 1200, "HR"),
    Employee("Lân", 1100, "IT"),
    Employee("Trung", 900, "HR"),
]

# Tính tổng lương theo phòng ban
totals = {}
for e in employees:
    totals[e.department] = totals.get(e.department, 0) + e.salary

# In kết quả
for dept, total in totals.items():
    print(f"Department: {dept}, Total Salary: {total}")
