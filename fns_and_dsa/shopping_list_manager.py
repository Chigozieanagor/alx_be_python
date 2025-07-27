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
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add = input("select an item to add (shoe, bags, phone): ")
            shopping_list.append(add)
            #print(shopping_list)
        elif choice == 2:
            sub = input("Select an item to remove: (shoe, bags, phone)")
            shopping_list.remove(sub)
            #print(shopping_list)
        elif choice == 3:
            view = shopping_list[::]
            print(view)

        elif choice == 4:
            print("Good bye")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
