

def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the name of the item to add: ").strip()
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

def remove_item(shopping_list):
    item = input("Enter the name of the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' was not found in the shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("Current Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
    else:
        print("Your shopping list is currently empty.")

def shopping_list_manager():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if name == "main":
    shopping_list_manager()
