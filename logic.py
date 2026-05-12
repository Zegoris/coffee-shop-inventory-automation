from models import Product

class InventoryManager:
    def __init__(self, products):
        self.products = products

    def add_product(self, name, category, quantity, price, min_limit):
        new_prod = Product(name, category, quantity, price, min_limit)
        self.products.append(new_prod)
        return True

    def sell_product(self, name, amount):
        for p in self.products:
            if p.name.lower() == name.lower():
                if p.quantity >= amount:
                    p.quantity -= amount
                    return True, f"Продано {amount} ед. {p.name}"
                return False, "Ошибка: недостаточно товара на складе!"
        return False, "Ошибка: товар не найден."

    def get_low_stock(self):
        return [p for p in self.products if p.quantity <= p.min_limit]