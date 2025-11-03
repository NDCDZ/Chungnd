# Lab 3: Book Class
# -----------------------
# Yêu cầu:
# 1. Xây dựng class Book với các thuộc tính: title, author, price, yearPublished
# 2. Viết chương trình lọc sách xuất bản sau năm 2020
# 3. In danh sách kết quả

class Book:
    def __init__(self, title, author, price, yearPublished):
        self.title = title
        self.author = author
        self.price = price
        self.yearPublished = yearPublished

books = [
    Book("Chung đẹp trai", "Chung", 15.5, 2019),
    Book("Hải dớ", "Hải", 22.0, 2021),
    Book("NDC Đức Chung", "Chung", 30.0, 2022),
    Book("What are u doing", "Lân", 18.0, 2018)
]

# Lọc sách xuất bản sau năm 2020
recent_books = [b for b in books if b.yearPublished > 2020]

# In kết quả
print("Books published after 2020:")
for b in recent_books:
    print(f"{b.title} by {b.author} ({b.yearPublished}) - ${b.price}")
