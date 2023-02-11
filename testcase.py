from cashier import Transaction

user = Transaction()

# Test Case 1
# Add Item 1
print("Test Case 1")
print("-----------------------------------------------------------------------")
user.add_item("Ayam Goreng", 2, 20_000)
print("\n")
# Add Item 2
user.add_item("Pasta Gigi", 3, 15_000)
print("\n")
print("Tabel transaksi:")
user.check_order()

# Test Case 2
# Delete pasta gigi from order table
print("\n")
print("Test Case 2")
print("-----------------------------------------------------------------------")
user.delete_item("Pasta Gigi")

# Test Case 3
# Reset all transaction
print("\n")
print("Test Case 3")
print("-----------------------------------------------------------------------")
user.reset_transaction()

# Test Case 4
# Total Transaction
user = Transaction()
print("\n")
print("Test Case 4")
print("-----------------------------------------------------------------------")
# Add Item 1
user.add_item("Ayam Goreng", 2, 20_000)
print("\n")
# Add Item 2
user.add_item("Pasta Gigi", 3, 15_000)
print("\n")
# Add Item 3
user.add_item("Mainan Mobil", 1, 200_000)
print("\n")
# Add Item 4
user.add_item("Mie Instan", 5, 3_000)
print("\n")
print("Tabel transaksi:")
user.check_order()
user.total_price()

# Test Case 5
# Update Item, Quantity, dan Harga
print("\n")
print("Test Case 5")
print("--------------------------------------------------------------------------")
print("Tabel Pemesanan Sebelum Update:")
user.check_order()
user.total_price()
print("\n")
# Update Item pasta gigi
user.update_item_name("Pasta Gigi", "Face Wash")
# Update Quantity mie instan
user.update_item_quantity("Mie Instan", 8)
# Update Harga mainan mobil
user.update_item_price("Mainan Mobil", 230_000)
print("\n")
print("Tabel Pemesanan Setelah Update:")
user.check_order()
user.total_price()