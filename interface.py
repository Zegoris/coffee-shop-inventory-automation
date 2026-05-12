def show_menu():
    print("\n" + "="*30)
    print("   УЧЕТ ЗАПАСОВ КОФЕЙНИ")
    print("="*30)
    print("1. Показать склад")
    print("2. Добавить товар")
    print("3. Оформить продажу")
    print("4. Проверить дефицит")
    print("5. Сохранить и выйти")
    return input("\nВыберите действие: ")

def display_inventory(products):
    if not products:
        print("\nСклад пуст.")
        return
    print(f"\n{'Название':<18} | {'Категория':<12} | {'Кол-во':<8} | {'Цена':<8}")
    print("-" * 55)
    for p in products:
        print(f"{p.name:<18} | {p.category:<12} | {p.quantity:<8} | {p.price:<8.2f}")

def get_product_input():
    print("\n--- Ввод нового товара ---")
    name = input("Название: ")
    category = input("Категория: ")
    qty = int(input("Текущее количество: "))
    price = float(input("Цена продажи: "))
    limit = int(input("Минимальный порог (для уведомлений): "))
    return name, category, qty, price, limit

def get_sale_input():
    name = input("\nВведите название товара для продажи: ")
    qty = int(input("Введите количество: "))
    return name, qty

def show_message(message):
    print(f"\n>>> {message}")

def show_low_stock_report(low_stock_list):
    if not low_stock_list:
        print("\n[OK] Все товары в достаточном количестве.")
    else:
        print("\n[!] ВНИМАНИЕ: СРОЧНАЯ ЗАКУПКА:")
        for p in low_stock_list:
            print(f" - {p.name}: осталось {p.quantity} (порог {p.min_limit})")