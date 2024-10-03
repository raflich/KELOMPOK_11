# Menu Makanan
class MenuMakanan:
    def init(self, name, price):
        self.name = name
        self.price = price

    def display_menu(self):
        print(f"Menu Name: {self.name}")
        print(f"Price: {self.price}")

    def get_price(self):
        return self.price

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

# Membuat menu makanan
menu1 = MenuMakanan("Nasi Goreng", 15000)
menu2 = MenuMakanan("Mie Ayam", 12000)
menu3 = MenuMakanan("Sate", 18000)

# Membuat order makanan
order = OrderMakanan()

# Membuat makanan yang akan diorder
order.add_menu(menu1)
order.add_menu(menu2)
order.add_menu(menu3)

# Detail dari order
order.display_order()

# Menghilangkan menu dari order
order.remove_menu("Mie Ayam")

# Menampilkan orderan kembali
order.display_order()