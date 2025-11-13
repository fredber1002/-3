class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name}: {self.price} ₽"

class Order:
    def __init__(self):
        self.items = []
        self.total_cost = 0

    def add_product(self, product):
        self.items.append(product)
        self.total_cost += product.price

    def del_product(self, product_name):
        for p in self.items:
            if p.name == product_name:
                self.items.remove(p)
                self.total_cost -= p.price
                return
        print("Товар не найден!")

    def print_receipt(self):
        print("┏══════ ЧЕК ══════┓")
        for p in self.items:
            print("┃", p.get_info(), "  ┃")
        print("┃☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲┃")
        print(f"┃Итого: {self.total_cost:.2f} ₽.┃")
        print("┕═════════════════┙")

products_list = [
    ("Хлеб", 59.99),
    ("Молоко", 129.99),
    ("Яблоки", 259),
    ("Сыр", 2199.9)
]

order = Order()

for name, price in products_list:
    order.add_product(Product(name, price))

order.del_product("Молоко")
order.print_receipt()