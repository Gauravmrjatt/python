import os
import time
from colorama import Fore, Back, Style


USERNAME = "123"
PASSWORD = "123"


shop_items = {}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Admin Login~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    user = input(Fore.YELLOW + '👤 Enter your Username : ')
    password = input('🔑 Enter your Password : ')
    if user == USERNAME and password == PASSWORD:
        print(Fore.GREEN + 'Login Success ✅')
        time.sleep(1)
        return True
    else:
        print(Fore.RED + "Invalid Username or Password")
        return False

def add_item():
    global shop_items
    item_id = int(input("Enter the Item ID : "))
    item_name = input("Enter the name of the Item : ")
    price = int(input("Enter the Price of the Item : ₹"))
    quantity = int(input("Enter the Quantity available in Stock : "))
    shop_items[item_id] = {
        "name": item_name,
        "price": price,
        "quantity": quantity
    }
    print(Fore.GREEN + "Item Added Successfully!")
    input("Press Enter to continue...")
    show_menu()

def show_items():
    print(Fore.BLUE + f"Items Available for Sale ({len(shop_items)})")
    print(Fore.YELLOW + "ID\tName\tPrice\tStock")
    for key, value in shop_items.items():
        print(f"{key}\t{value['name']}\t{value['price']}\t{value['quantity']}")
    print(Style.RESET_ALL)

def delete_item():
    global shop_items
    show_items()
    item_to_delete = int(input("Enter Item Id : "))
    if item_to_delete in shop_items:
        del shop_items[item_to_delete]
        print(Fore.RED + "Item Deleted Successfully!")
    else:
        print(Fore.RED + "No such Item Found.")
    input("Press Enter to continue...")
    show_menu()

def update_item():
    global shop_items
    show_items()
    item_id = int(input("Enter Item ID : "))
    if item_id in shop_items:
        name = input("Enter New Name (Optional): ")
        if name:
            shop_items[item_id]['name'] = name
        price = float(input("Enter new Price (Optional): "))
        if price:
            shop_items[item_id]['price'] = price
        quantity = int(input("Enter the number of items to add or remove (-ve/+ve).\nEnter 0 to skip: "))
        if quantity:
            shop_items[item_id]['quantity'] += quantity
        print(Fore.GREEN + "Item Updated Successfully!")
    else:
        print(Fore.RED + "No such Item Found.")
    input("Press Enter to continue...")
    show_menu()

def show_menu():
    clear_screen()
    print(Fore.BLUE + "Please select from the menu:\n")
    print(Back.YELLOW + " Operation      :   Press          ")
    print(Style.RESET_ALL)
    print(Fore.MAGENTA + "Add New Item   :   1 ")
    print("Delete Item    :   2 ")
    print("Update Item    :   3 ")
    print("View All Items :   4 ")
    print(Fore.LIGHTBLUE_EX)
    user_choice = input("\nEnter Your Choice (Number): ")

    if user_choice == '1':
        clear_screen()
        add_item()
    elif user_choice == '2':
        clear_screen()
        delete_item()
    elif user_choice == '3':
        clear_screen()
        update_item()
    elif user_choice == '4':
        clear_screen()
        show_items()
        input("\nPress Enter to continue...")
        show_menu()
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
        input("Press Enter to continue...")
        show_menu()


if __name__ == "__main__":
    clear_screen()
    print(Fore.YELLOW + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~Welocome to Shop~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    if login():
        show_menu()


