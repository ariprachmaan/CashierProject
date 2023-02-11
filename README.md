# Cashier Project

Program Cashier sederhana yang dibuat dengan bahasa pemrograman python.

## Background Problem

Pak Andi merupakan pemilik salah satu supermarket besar yang ada di salah satu kota di Indonesia. Pak Andi ingin melakukan perbaikan dan pengembangan untuk supermarket tersebut. Untuk itu Pak Andi ingin membuat sistem kasir yang self-service di supermarketnya, sehingga customer bisa langsung memasukkan item, jumlah item dan harga item yang akan dibeli serta fitur lainnya. Tujuannya untuk mempermudah semua customer yang berbelanja di supermarket tersebut.

## Requirements/Objectives

- Membuat sistem untuk proses transaksi pada self-service kasir
- Membuat proses untuk menambahkan item dengan parameter nama item, jumlah item dan harga item
- Membuat proses untuk mengupdate dari nama item, jumalah item dan harga item
- Membuat proses untuk menghapus pesanan dan mereset transaksi yang sudah dilakukan
- Membuat proses untuk mengecek orderan dari costumer
- Membuat total pembayaran untuk mengecek apakah mendapatkan diskon atau tidak untuk pesanan tersebut

## Flowchart/Alur Program

![Flowchart Cashier](img/Flowchart%20Cashier.png)

## Cara Penggunaan Program

- Download semua file/module Python ke dalam satu direktori lokal.
- Buka terminal dan sesuaikan lokasi direktori lokal.
- Jalankan module python Cashier.py di terminal.
- Output akan ditampilkan sesuai case yang akan dijalankan

### Penjelasan dari Code

Script Cashier.py berfungsi untuk menjalankan program yang berisi function berikut :

#### Class Transaction
Class Transaction akan menjadi class yang berisikan method/function untuk melakukan seluruh proses transaksi

#### init()
Fungsi inisialisasi untuk class Transaction
order = dictionary untuk menyimpan data transaksi (dict)

#### Add_item
Fungsi untuk menambahkan nama_item, jumlah_item, harga_item ke dalam attribute class data            
Parameter:
nama_item (str)   : name of the groceries item
jumlah_item (int) : quantity of the groceries item
harga_item (int)  : each price of the groceries item

#### Update_item_name
Fungsi untuk memperbarui/mengganti nama_item         
Parameter:
nama_item (str)       : name of the groceries item
nama_item_baru (str)  : updated name of the groceries item

#### Update_item_quantity
Fungsi untuk memperbarui/mengganti jumlah_item 
Parameter:
nama_item (str)         : name of the groceries item
update_jumlah_item (int): updated quantity of the groceries item

#### Update_item_price
Fungsi untuk menmperbarui/mengganti harga 
Parameter:
nama_item (str)   : name of the groceries item
update_harga (int): updated price of the groceries item

#### Delete_item
Fungsi untuk menghapus item 

Parameter:
nama_item (str): name of the groceries item

#### Reset_transaction
Fungsi untuk menghapus semua item yang ada dalam attribute class data

#### Check_order
Fungsi untuk mengecek kembali item yang telah diinputkan

#### Display
Fungsi untuk menampilkan table yang berisikan data yang sudah diinput

#### Total_price
Fungsi untuk menampilkan table yang berisikan data yang sudah diinput

## Test Case
- Harap menjalankan terlebih dahulu cashier.py
- Untuk hasil test case bisa dijalankan diterminal ataupun dilihat dari notebook document

## Conclusion
Dari hasil pengerjaan project self-service cashier ini, diharapkan bisa membantu dan digunakan oleh pembeli sehingga pembeli dapat merasakan pengalaman baru dalam berbelanja

## Future Work
Untuk kedepannya diharapkan program ini bisa lebih komplex lagi dengan menambahkan beberapa fitur seperti item-item yang sudah diinput sehingga lebih cepat lagi dalam memproses pembelian item tersebut