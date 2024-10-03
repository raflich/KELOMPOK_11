# CLass menu makanan
class MenuMakanan:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Method menu
    def display_menu(self):
        print(f"Menu Name: {self.name}")
        print(f"Price: {self.price}")

    def get_price(self):
        return self.price