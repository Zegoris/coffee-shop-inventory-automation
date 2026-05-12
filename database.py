import json
import os
from models import Product

DB_FILE = "inventory.json"

def save_to_file(products):
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in products], f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")

def load_from_file():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Product(**item) for item in data]
    except Exception as e:
        print(f"Ошибка при чтении базы данных: {e}")
        return []