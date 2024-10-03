# Order Makanan
class OrderMakanan:
    def init(self):
        self.menu_list = []

    def add_menu(self, menu):
        self.menu_list.append(menu)
        print(f"Menu {menu.name} added to order")

    def remove_menu(self, menu_name):
        for menu in self.menu_list:
            if menu.name == menu_name:
                self.menu_list.remove(menu)
                print(f"Menu {menu_name} removed from order")
                return
        print(f"Menu {menu_name} not found in order")

    def calculate_total(self):
        total_price = 0
        for menu in self.menu_list:
            total_price += menu.get_price()
        return total_price

    def display_order(self):
        print("Order Details:")
        for menu in self.menu_list:
            menu.display_menu()
        print(f"Total Price: {self.calculate_total()}")

