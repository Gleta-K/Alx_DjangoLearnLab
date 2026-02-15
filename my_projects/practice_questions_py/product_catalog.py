class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = int(price)
        self.quantity = int(quantity)
    def total_value(self):
        total = int(self.price * self.quantity)
        return total
product1 = Product("maize flour", "500", 2)
print(product1.total_value())