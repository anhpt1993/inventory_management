# good = {1: "táo",
#         2: "xoài",
#         3: "cam"}

from module_add import add_item

def choose_option():
    while True:
        try:
            option = int(input("""
            Choose one of the following option:
            1. Show all goods
            2. Add new merchandise
            3. Update
            4. Delete
            5. Exit
            
            => Your choice: """))
            if 1 <= option <= 5:
                return option
                break
            else:
                print("\nInvalid Value. Try Again!!!\n")
        except ValueError:
            print("\nInvalid Value. Try Again!!!\n")
def try_again(text):
    answer = input(text).upper()
    if answer == "Y" or answer == "YES":
        return True
    else:
        return False

def choose_item(goods):
    while True:
        try:
            value = int(input())
            if value in list(goods.keys()):
                return value
                break
            else:
                print("\nS/N {value} is not in your ID management\n")
        except ValueError:
            print("\nInvalid Value. Try Again!!!\n")

if __name__ == '__main__':
    goods = {}
    while True:
        option = choose_option()
        if option == 2:
            if bool(goods):
                goods.update({max(goods.keys()) + 1: add_item()})
            else:
                goods.update({1: add_item()})
        elif option == 5:
            exit()
        else:
            if bool(goods):
                if option == 1:
                    print("Your total merchandise: ")
                    for key, val in goods.items():
                        print(f"{key}: {val}")
                elif option == 3:
                    print("Enter a serial number to update: ")
                    serial = choose_item(goods)
                    new_value = input("New item name: ")
                    goods[serial] = new_value
                elif option == 4:
                    print("Enter a serial number to delete: ")
                    serial = choose_item(goods)
                    del goods[serial]
            else:
                print("\nEmpty inventory. You have to import something!!!\n".upper())