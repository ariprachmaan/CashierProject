# import the library will be use
import pandas as pd
from tabulate import tabulate

class Transaction:
    """Fungsi sistem kasir"""
  
    # Utilised class function to store the attribute and method requires to create a self-service cashier
    def __init__(self):
      """
      Fungsi menginisialisasi transaksi costumer
    
      """
      # Empty Dictionary
      self.order = {}

    def add_item(
        self, nama_item, jumlah_item, harga_item
        ):
        """
        Fungsi untuk menambahkan nama_item, jumlah_item, harga_item ke dalam attribute class data
            
          Parameter:
          nama_item (str)   : name of the groceries item
          jumlah_item (int) : quantity of the groceries item
          harga_item (int)  : each price of the groceries item

        """

        # Check type of data parameter nama_item, jumlah_item dan harga_item
        if type(nama_item) != str:
            raise TypeError(
                "Mohon masukkan nama item sesuai dengan format"
            )
        elif type(jumlah_item) != int:
            raise TypeError(
                "Mohon masukkan jumlah item sesuai dengan format"
            )
        elif type(harga_item) != int:
            raise TypeError(
                "Mohon masukkan harga item sesuai dengan format"
            )
        else:
          # Update order dictionary
          order_add = {nama_item: [jumlah_item, harga_item, jumlah_item*harga_item]}
          self.order.update(order_add)
          print("Masukkan item yang akan dibeli")
          print(f"Nama Item     : {nama_item}")
          print(f"Jumlah Item   : {jumlah_item}")
          print(f"Harga per-Item: Rp. {harga_item}")

    def update_item_name(self, nama_item, nama_item_baru):
        """
        Fungsi untuk memperbarui/mengganti nama_item 
        
        Parameter:
            nama_item (str)       : name of the groceries item
            nama_item_baru (str)  : updated name of the groceries item

        """
        # Check type of data parameter nama item baru
        if type(nama_item_baru) != str:
            raise TypeError(
                "Mohon masukkan nama item sesuai dengan format"
                )
        else:
          # Mengganti nama item dengan nama item baru 
          temp = self.order[nama_item]
          self.order.pop(nama_item)
          self.order.update({nama_item_baru: temp})

          # Menampilkan update nama item baru
          self.display()
          print(f"Anda mengganti item {nama_item} menjadi {nama_item_baru}")

    def update_item_quantity(self, nama_item, jumlah_item_baru):
        """
        Fungsi untuk memperbarui/mengganti jumlah_item 

          Parameter:
            nama_item (str)         : name of the groceries item
            update_jumlah_item (int): updated quantity of the groceries item

        """
        # Check type of data parameter jumlah item baru
        try:
          if type(jumlah_item_baru) != int:
            raise TypeError(
                "Mohon masukkan jumlah item sesuai dengan format"
                        )
          else:
            # Mengganti jumlah item dengan jumlah item baru
            self.order[nama_item][0] = jumlah_item_baru
            self.order[nama_item][2] = jumlah_item_baru * self.order[nama_item][1]

            # Menampilkan update nama jumlah item baru
            self.display()
            print(f"Anda mengganti jumlah item {nama_item} menjadi {jumlah_item_baru}")

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam transaksi")
        
    def update_item_price(self, nama_item, harga_item_baru):
        """
        Fungsi untuk menmperbarui/mengganti harga 

          Parameter:
            nama_item (str)   : name of the groceries item
            update_harga (int): updated price of the groceries item
        
        """
        # Check type of data parameter harga item baru
        try:
          if type(harga_item_baru) != int:
            raise TypeError(
                "Mohon masukkan jumlah item sesuai dengan format"
                )
          else:
            # Mengganti harga item dengan harga item baru                
            self.order[nama_item][1] = harga_item_baru
            self.order[nama_item][2] = harga_item_baru * self.order[nama_item][0]

            # Menampilkan update harga item baru
            self.display()
            print(f"Anda mengganti jumlah item {nama_item} menjadi {harga_item_baru}")

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam transaksi")

    def delete_item(self, nama_item: str):
        """
        Fungsi untuk menghapus item 

          Parameter:
            nama_item (str): name of the groceries item
        
        """
        try:
          # Menghapus data nama item beserta jumlah dan harganya dalam dictionary
          self.order.pop(nama_item)

          # Menampilkan data yang dihapus
          print(f"Anda telah menghapus item {nama_item} dari transaksi")
          print("")
          return self.display()

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam riwayat transaksi")

    def reset_transaction(self):
        """
        Fungsi untuk menghapus semua item yang ada dalam attribute class data

        """
        # Menghapus semua item yang ada dalam dictionary
        self.order = self.order.clear()
        print("Semua item berhasil di delete!")
        return self.display()
    
    def check_order(self):
        """
        Fungsi untuk mengecek kembali item yang telah diinputkan

          Return:
            Terdapat kesalahan input data = There is a data input error
            Pemesanan sudah benar = Correct order
            
        """
        for key, values in self.order.items():
            nama_item   = key
            jumlah_item = values[0]
            harga_item  = values[1]

        if type(key) != str and values[0] != int and values[1] != int:
             print("Terdapat kesalahan input data, Mohon masukkan nama item sesuai dengan format")

        elif(len(self.order) == 0):
            print('Tidak ada pesanan yang dibuat')

        else:
            print("Pemesanan sudah benar")
            return self.display()

    def display(self):
        """
        Fungsi untuk menampilkan table yang berisikan data yang sudah diinput

        """      
        # Menampikan display pesanan
        table = pd.DataFrame(self.order).T
        data_colomn = ["Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
        print(tabulate(table, headers = data_colomn, tablefmt="psql", stralign="center"))
  
    def total_price(self):
        """
        Fungsi untuk menghitung total transaksi dari item yang diinputkan, termasuk diskon yang diperoleh
        
          Return:
            int : total transaction
        """

        # Membuat total pembelanjaan
        transaksi = self.order.copy()
        total = sum(transaksi[nama_item][2] for nama_item in transaksi)  

        # Jika total pembelanjaan di bawah 200000 mendapatkan harga normal
        if total >= 0 and total <= 200_000:
            return print(f"Total pembayaran sebesar Rp.{int(total)}")

        # Jika total pembelanjaan lebih dari 200000 dan kurang dari 300000
        # Mendapatkan diskon 5%
        elif total > 200_000 and total <= 300_000:
            total_belanja = total * 0.95
            return print(
                f"Total Harga item sebesar Rp.{int(total)} \nAnda mendapatkan diskon sebesar 5% \nTotal pembayaran sebesar Rp.{int(total_belanja)} \nTerima kasih sudah berbelanja"
            )

        # Jika total pembelanjaan lebih dari 300000 dan kurang dari 500000
        # Mendapatkan diskon 8%
        elif total > 300_000 and total <= 500_000:
            total_belanja = total * 0.92
            return print(
                f"Total Harga item sebesar Rp.{int(total)} \nAnda mendapatkan diskon sebesar 8% \nTotal pembayaran sebesar Rp.{int(total_belanja)} \nTerima kasih sudah berbelanja"
            )

        # Jika total pembelanjaan lebih dari 500000, mendapatkan diskon 10%
        elif total > 500_000:
            total_belanja = total * 0.90
            return print(
                f"Total Harga item sebesar Rp.{int(total)} \nAnda mendapatkan diskon sebesar 10% \nTotal pembayaran sebesar Rp.{int(total_belanja)} \nTerima kasih sudah berbelanja"
            )
        else:
            return "Anda belum melakukan transaksi, mohon melakukan transaksi terlebih dahulu"