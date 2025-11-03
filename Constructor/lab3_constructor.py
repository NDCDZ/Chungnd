# Lab 3: Order Class (Constructor with List)
class Order:
    def __init__(self, products):
        self.products = products
        self.total = sum(p['price'] for p in products)

    def show_order(self):
        print("Order details:")
        for p in self.products:
            print(f"- {p['name']}: ${p['price']}")
        print(f"Total: ${self.total}")

if __name__ == "__main__":
    order = Order([{'name': 'Keyboard', 'price': 50}, {'name': 'Mouse', 'price': 20}])
    order.show_order()
