def add_item():
    return input("Enter the name of item: ")

if __name__ == '__main__':
    goods = {}
    if bool(goods):
        goods.update({max(goods.keys) + 1: add_item()})
    else:
        goods.update({1: add_item()})

    print(goods)