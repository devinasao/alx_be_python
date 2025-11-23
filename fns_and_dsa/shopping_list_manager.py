def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()

        # ✅ CHANGED SECTION: convert choice to an integer + validation
        try:
            choice = int(input("Enter your choice (number): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.\n")
            continue
        # ---------------------------------------------

        if choice == 1:
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.\n")
            else:
                print("No item entered. Please try again.\n")

        elif choice == 2:
            if not shopping_list:
                print("The list is empty — nothing to remove.\n")
                continue
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.\n")
            else:
                print("Item not found in the list.\n")

        elif choice == 3:
            print("Your Shopping List:")
            if not shopping_list:
                print(" - The list is empty.\n")
            else:
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
                print()

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()
