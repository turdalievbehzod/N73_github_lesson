import json
import os

def load_data():
    if os.path.exists("electronics_store.json"):
        with open("electronics_store.json", "r") as file:
            return json.load(file)
    else:
        return {
            "phones": [
                {"name": "iPhone 14", "price": "999", "year": "2022"},
                {"name": "Samsung Galaxy S23", "price": "850", "year": "2023"}
            ],
            "tvs": [
                {"name": "LG OLED CX", "price": "1200", "year": "2021"},
                {"name": "Samsung QLED Q90T", "price": "1400", "year": "2020"}
            ],
            "computers": [
                {"name": "MacBook Pro", "price": "1800", "year": "2023"},
                {"name": "Dell XPS 15", "price": "1500", "year": "2022"}
            ]
        }

def save_data(store):
    with open("electronics_store.json", "w") as file:
        json.dump(store, file, indent=4)


def add_product(store: dict):
    print("\nChoose category to add product:")
    print("1. Phone")
    print("2. TV")
    print("3. Computer")
    choice = input("Enter number: ")

    if choice == "1":
        category = "phones"
    elif choice == "2":
        category = "tvs"
    elif choice == "3":
        category = "computers"
    else:
        print("Invalid choice.")
        return

    name = input("Enter product name: ")
    price = input("Enter price (in USD): ")
    year = input("Enter year of release: ")

    new_item = {
        "name": name,
        "price": price,
        "year": year
    }

    store[category].append(new_item)
    save_data(store)
    print(f"{name} added successfully to {category}!")


def view_all(store: dict):
    print("\nAll Electronics")
    for category, items in store.items():
        print(f"\n{category.capitalize()}:")
        if not items:
            print("  (No items yet)")
        for item in items:
            print(f"  Name: {item['name']}, Price: ${item['price']}, Year: {item['year']}")


def view_category(store: dict):
    print("\nChoose category to view:")
    print("1. Phones")
    print("2. TVs")
    print("3. Computers")
    choice = input("Enter number: ")

    if choice == "1":
        category = "phones"
    elif choice == "2":
        category = "tvs"
    elif choice == "3":
        category = "computers"
    else:
        print("Invalid choice.")
        return

    print(f"\n{category.capitalize()}")
    if not store[category]:
        print("No items found.")
    else:
        for item in store[category]:
            print(f"Name: {item['name']}, Price: ${item['price']}, Year: {item['year']}")


def store_manager(store: dict):
    while True:
        print("\nOnline Electronics Store")
        print("1. View all electronics")
        print("2. View certain type of electronics")
        print("3. Add new electronics")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_all(store)
        elif choice == "2":
            view_category(store)
        elif choice == "3":
            add_product(store)
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print("Invalid option, please try again.")

electronics = load_data()
store_manager(electronics)
