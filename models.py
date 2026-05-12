class Product:
    def __init__(self, name, category, quantity, price, min_limit):
        self.name = str(name)
        self.category = str(category)
        self.quantity = int(quantity)
        self.price = float(price)
        self.min_limit = int(min_limit)

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price,
            "min_limit": self.min_limit
        }