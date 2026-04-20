
# stock_manager.py
# Exercise: debug-errors-001
# Fixed by exercise participant:
# - Identified and corrected an off-by-one error in the loop range
# - Ensured inventory iteration stays within valid list indices

def print_inventory_report(items):
    print("===== INVENTORY REPORT =====")
    for i in range(len(items)):
        print(f"Item {i+1}: {items[i]['name']} - Quantity: {items[i]['quantity']}")
    print("============================")

def main():
    items = [
        {"name": "Laptop", "quantity": 15},
        {"name": "Mouse", "quantity": 30},
        {"name": "Keyboard", "quantity": 25},
    ]

    print_inventory_report(items)

if __name__ == "__main__":
    main()
