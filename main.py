import database
import interface
from logic import InventoryManager

def main():
    products = database.load_from_file()
    manager = InventoryManager(products)

    while True:
        choice = interface.show_menu()

        if choice == "1":
            interface.display_inventory(manager.products)

        elif choice == "2":
            try:
                data = interface.get_product_input()
                manager.add_product(*data)
                interface.show_message("Товар добавлен!")
            except ValueError:
                interface.show_message("Ошибка: вводите корректные числа!")

        elif choice == "3":
            try:
                name, qty = interface.get_sale_input()
                success, message = manager.sell_product(name, qty)
                interface.show_message(message)
            except ValueError:
                interface.show_message("Ошибка ввода количества!")

        elif choice == "4":
            low_stock = manager.get_low_stock()
            interface.show_low_stock_report(low_stock)

        elif choice == "5":
            database.save_to_file(manager.products)
            interface.show_message("Данные сохранены. До свидания!")
            break
        else:
            interface.show_message("Неверный пункт меню.")

if __name__ == "__main__":
    main()