'''
=================================================
Graded Challenge 2

Nama  : Kamelia Ramandha
Batch : CODA-RMT-001

Program ini dibuat untuk membuat program sederhana untuk user memasukan, menghapus, menampilkan, dan menghitung barang pada shopping cart menggunakan if, loop, dan function.
=================================================
'''


cart = {}
dict_items = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'anggur': 6500, 'semangka': 10000, 'melon': 12000, 'kiwi': 15000}

def add_to_cart():
    ''' Fungsi ini digunakan untuk menambahkan barang ke dalam keranjang belanja '''

    #fungsi di bawah digunakan untuk membuat dictionary barang dan menampilkan barang yang tersedia di toko
    print("Barang yang tersedia di toko kami:")
    for barang, harga in dict_items.items():
        print(f" - {barang}: Rp.{harga}")

    #fungsi di bawah digunakan untuk menambahkan barang ke dalam keranjang
    item = input("Masukkan nama barang yang ingin ditambahkan: ").lower()
    price = dict_items.get(item)
    qty = 0
    
    #fungsi di bawah digunakan untuk validasi input user
    if item == None:
        print("Mohon masukan nama barang yang ingin ditambahkan")
    elif item not in dict_items.keys():
        print(f"{item} tidak tersedia di toko kami")
    else:
        print(f"{item} dengan harga {price} berhasil ditambahkan ke dalam keranjang")
        if item in cart:
            cart[item]["qty"] += 1 #jika barang sudah ada di keranjang, maka qty akan bertambah 1
        else:
            cart[item] = {"harga": price, "qty": 1} #jika barang belum ada di keranjang, maka akan ditambahkan ke keranjang dengan qty 1

def delete_item():
    ''' Fungsi ini digunakan untuk menghapus barang dari keranjang belanja '''
    
    #fungsi di bawah digunakan untuk melihat apakah ada barang di keranjang
    if not cart:
        print("Keranjang kosong, tidak ada barang yang bisa dihapus.")
        return
    
    #fungsi di bawah digunakan untuk menampilkan barang yang ada di keranjang
    print("Barang di keranjang:")
    for i, (item, details) in enumerate(cart.items(), start=1):
        print(f"{i}. {item}: Rp.{details["harga"]} x {details["qty"]}")

    #fungsi di bawah digunakan untuk menghapus barang dari keranjang
    item = input("Masukkan nama barang yang ingin dihapus: ").lower()
    
    if item in cart:
        if cart[item]["qty"] > 1: #jika qty barang lebih dari 1, maka qty akan dikurangi 1
            cart[item]["qty"] -= 1
            print(f"Jumlah {item} dikurangi 1 (sisa {cart[item]['qty']})")
        else: #jika qty barang 1, maka barang akan dihapus dari keranjang
            del cart[item]
            print(f"Barang {item} berhasil dihapus dari keranjang")
    else: #jika barang tidak ada di keranjang, maka akan menampilkan pesan error
        print(f"Barang {item} tidak ditemukan dalam keranjang")

def view_cart():
    ''' Fungsi ini digunakan untuk menampilkan barang yang ada di dalam keranjang belanja '''
    #fungsi di bawah digunakan untuk melihat apakah ada barang di keranjang
    if not cart:
        print("Keranjang belanja Anda kosong.")

    #fungsi di bawah digunakan untuk menampilkan barang yang ada di keranjang
    else:
        print("Barang di keranjang:")
        for i, (item, details) in enumerate(cart.items(), start=1):
            print(f"{i}. {item}: Rp.{details["harga"]} x {details["qty"]}")

def total_price():
    ''' Fungsi ini digunakan untuk menghitung total harga dari barang yang ada di dalam keranjang belanja '''
    
    #fungsi di bawah digunakan untuk melihat apakah ada barang di keranjang
    if not cart:
        print("Keranjang belanja Anda kosong.")
    #fungsi di bawah digunakan untuk menghitung total harga dari barang yang ada di keranjang
    else:
        total = sum(item['harga'] * item['qty'] for item in cart.values())
        print(f"Total belanja: Rp.{total}")

def menu():
    ''' Fungsi ini digunakan untuk menampilkan menu utama dan mengarahkan user ke fungsi yang diinginkan '''
    #fungsi di bawah digunakan untuk menampilkan menu utama
    print("Selamat Datang di Keranjang Belanja Toko Makmur!")
    print("Menu: \n 1. Menambah Barang \n 2. Hapus Barang \n 3. Tampilkan Barang di Keranjang \n 4. Lihat Total Belanja \n 5. Exit")
    
    #fungsi di bawah digunakan untuk mengarahkan user ke fungsi
    input_menu = input("Masukkan nomor menu yang ingin Anda pilih: ")
    
    #fungsi di bawah untuk memindahkan user ke fungsi yang diinginkan
    while input_menu == "1":
        add_to_cart()
        add_again = input("Apakah Anda ingin menambah barang lagi? (ya/tidak): ").lower() #validasi input user
        if add_again == "ya": #jika user menjawab ya, maka akan kembali ke fungsi add_to_cart
            continue
        elif add_again == "tidak": #selain itu, user akan kembali ke menu utama
            print("Anda akan kembali ke menu utama.\n")
            break
        else:
            print("Mohon masukkan jawaban yang sesuai (ya/tidak).")
    
    #fungsi di bawah untuk memindahkan user ke fungsi yang diinginkan
    while input_menu == "2":
        delete_item()
        delete_again = input("Apakah Anda ingin menghapus barang lagi? (ya/tidak) ").lower() #validasi input user
        if delete_again == 'ya': #jika user menjawab ya, maka akan kembali ke fungsi delete_item
            continue
        else: #selain itu, user akan kembali ke menu utama
            print("Anda akan kembali ke menu utama.\n")
            return menu()
        
    #fungsi di bawah untuk memindahkan user ke fungsi yang diinginkan
    while input_menu == '3':
        view_cart()
        back = input("Apakah anda ingin kembali ke menu utama? (ya/tidak) ") #validasi input user
        if back == 'ya':
            return menu()
        else:
            continue
    
    #fungsi di bawah untuk memindahkan user ke fungsi yang diinginkan
    while input_menu == '4':
        total_price()
        back = input("Apakah anda ingin kembali ke menu utama? (ya/tidak) ") #validasi input user
        if back == "ya":
            return menu()
        else:
            continue
    
    #fungsi di bawah untuk keluar dari program
    if input_menu == "5":
        print("Sampai Jumpa! Terima kasih telah berbelanja di Toko Makmur!")
    else:
        print("Mohon masukkan nomor menu yang sesuai.")
        return menu()


if __name__ == "__main__":
    menu()