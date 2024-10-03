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