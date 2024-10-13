# mengubah dari list ke dictionary
akun = {}
daftar_produk = {} 

while True:
    print("Selamat datang di TOKOSHOPI")
    print("=== Selamat datang di TOKOSHOPI ===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")

    opsi_input = input("Pilih opsi? (1/2/3): ").strip()
    print("")

    if not opsi_input:
        print("Input tidak boleh kosong. Silakan masukkan 1, 2, atau 3.\n")
    elif not opsi_input.isdigit():
        print("Input harus berupa angka. Silakan masukkan 1, 2, atau 3.\n")
    elif opsi_input not in ["1", "2", "3"]:
        print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.\n")
    else:
        if opsi_input == "1":  # Register
            print("Silahkan pilih role")
            print("1. Admin")
            print("2. User")
            regis_input = input("Pilih role anda?(1/2): ").strip()
            print("")

            if regis_input == "1":  # Admin
                admin_username = input("Masukkan username: ").strip()
                if admin_username in akun:
                    print("Username telah dipakai")
                else:
                    admin_password = input("Masukkan password: ").strip()
                    akun[admin_username] = {
                        "password": admin_password,
                        "role": "admin",
                        "produk": []
                    }
                    print("Akun admin anda telah terdaftar")

            elif regis_input == "2":  # User
                user_username = input("Masukkan username: ").strip()
                if user_username in akun:
                    print("Username telah dipakai")
                else:
                    user_password = input("Masukkan password: ").strip()
                    akun[user_username] = {
                        "password": user_password,
                        "role": "user",
                        "keranjang": []
                    }
                    print("Akun user anda telah terdaftar")
            else:
                print("Pilihan tidak valid. Silakan masukkan 1 atau 2.\n")

        elif opsi_input == "2":  # Login
            print("Pilih akun anda")
            print("1. Admin")
            print("2. User")
            login_input = input("Pilih role anda: ").strip()

            if login_input == "1":  # Login Admin
                admin_username = input("Masukkan username: ").strip()
                admin_password = input("Masukkan password: ").strip()

                if admin_username not in akun:
                    print("Username tidak ditemukan.")
                elif akun[admin_username]['password'] != admin_password:
                    print("Password salah.")
                elif akun[admin_username]['role'] != "admin":
                    print("Akun ini bukan akun admin.")
                else:
                    while True:
                        print(f"\nSelamat datang {admin_username}! ")
                        print("―――Silakan pilih menu!―――")
                        print("1. Menambah produk ")
                        print("2. Melihat produk  ")
                        print("3. Edit/ubah produk")
                        print("4. Hapus produk")
                        print("5. Exit")
                        print("―――――――――――――――――――――――――――――")

                        pilih = input("Pilih opsi: ").strip()
                        print(" ")

                        if pilih == "1":  # Tambah produk
                            nama_produk = input("Masukkan nama produk: ").strip()
                            deskripsi_produk = input("Masukkan deskripsi produk: ").strip()
                            stok_produk = input("Masukkan stok produk: ").strip()
                            harga_produk = input("Masukkan harga produk: ").strip()

                            if not nama_produk or not deskripsi_produk or not stok_produk or not harga_produk:
                                print("Semua data produk harus diisi.")
                            elif not stok_produk.isdigit() or not harga_produk.isdigit():
                                print("Stok dan harga harus berupa angka.")
                            else:
                                daftar_produk[nama_produk] = {  # Menambahkan produk ke dictionary
                                    "deskripsi": deskripsi_produk,
                                    "stok": int(stok_produk),
                                    "harga": int(harga_produk)
                                }
                                print("Produk berhasil ditambahkan.")

                        elif pilih == "2":  # Lihat produk
                            if not daftar_produk:
                                print("Tidak ada produk yang tersedia saat ini.")
                            else:
                                print("Daftar produk yang tersedia:")
                                for nama, produk in daftar_produk.items():
                                    print(f"Nama: {nama}, Deskripsi: {produk['deskripsi']}, Stok: {produk['stok']}, Harga: {produk['harga']}\n")

                        elif pilih == "3":  # Edit produk
                            if not daftar_produk:
                                print("Tidak ada produk untuk diedit.")
                            else:
                                input_edit = input("Masukkan nama produk yang ingin diedit: ").strip()

                                if input_edit in daftar_produk:
                                    print(f"Produk yang akan diedit: {daftar_produk[input_edit]}")

                                    nama_baru = input("Masukkan nama baru (Enter untuk tidak mengubah): ").strip()
                                    deskripsi_baru = input("Masukkan deskripsi baru (Enter untuk tidak mengubah): ").strip()
                                    stok_baru = input("Masukkan stok baru (Enter untuk tidak mengubah): ").strip()
                                    harga_baru = input("Masukkan harga baru (Enter untuk tidak mengubah): ").strip()

                                    if nama_baru:
                                        daftar_produk[nama_baru] = daftar_produk.pop(input_edit)  # Ganti nama produk
                                        if deskripsi_baru:
                                            daftar_produk[nama_baru]['deskripsi'] = deskripsi_baru
                                        if stok_baru and stok_baru.isdigit():
                                            daftar_produk[nama_baru]['stok'] = int(stok_baru)
                                        if harga_baru and harga_baru.isdigit():
                                            daftar_produk[nama_baru]['harga'] = int(harga_baru)

                                        print("Produk berhasil diedit.")
                                    else:
                                        if deskripsi_baru:
                                            daftar_produk[input_edit]['deskripsi'] = deskripsi_baru
                                        if stok_baru and stok_baru.isdigit():
                                            daftar_produk[input_edit]['stok'] = int(stok_baru)
                                        if harga_baru and harga_baru.isdigit():
                                            daftar_produk[input_edit]['harga'] = int(harga_baru)

                                        print("Produk berhasil diedit.")
                                else:
                                    print("Produk tidak ditemukan.")

                        elif pilih == "4":  # Hapus produk
                            input_hapus = input("Masukkan nama produk yang ingin dihapus: ").strip()

                            if input_hapus in daftar_produk:
                                del daftar_produk[input_hapus]
                                print("Produk berhasil dihapus.")
                            else:
                                print("Produk tidak ditemukan.")

                        elif pilih == "5":
                            print("Keluar dari aplikasi.\n")
                            break
                        else:
                            print("Input tidak valid, silakan pilih opsi yang tersedia.\n")

            elif login_input == "2":  # Login User
                user_username = input("Masukkan username: ").strip()
                user_password = input("Masukkan password: ").strip()

                if user_username not in akun:
                    print("Username tidak ditemukan.")
                elif akun[user_username]['password'] != user_password:
                    print("Password salah.")
                elif akun[user_username]['role'] != "user":
                    print("Akun ini bukan akun user.")
                else:
                    print(f"\nSelamat datang {user_username}!")

                    if not daftar_produk:
                        print("Tidak ada produk yang tersedia saat ini.")
                    else:
                        print("Daftar produk yang tersedia:")
                        for nama, produk in daftar_produk.items():
                            print(f"Nama: {nama}, Deskripsi: {produk['deskripsi']}, Stok: {produk['stok']}, Harga: {produk['harga']}\n")

                    while True:
                        print("―――Silakan pilih menu!―――")
                        print("1. Tambah produk ke keranjang ")
                        print("2. Melihat keranjang belanja  ")
                        print("3. Edit keranjang belanja")
                        print("4. Checkout")
                        print("5. Exit")
                        print("―――――――――――――――――――――――――――――")

                        pilih_user = input("Pilih opsi: ").strip()

                        if pilih_user == "1":  # Tambah produk ke keranjang
                            if not daftar_produk:
                                print("Tidak ada produk yang tersedia saat ini.")
                            else:
                                input_keranjang = input("Masukkan nama produk yang ingin dibeli: ").strip()
                                if input_keranjang in daftar_produk:
                                    produk_dipilih = daftar_produk[input_keranjang]
                                    if produk_dipilih['stok'] > 0:
                                        akun[user_username]['keranjang'].append({
                                            'nama': input_keranjang,
                                            'harga': produk_dipilih['harga']
                                        })
                                        daftar_produk[input_keranjang]['stok'] -= 1
                                        print(f"Produk {input_keranjang} berhasil ditambahkan ke keranjang.")
                                    else:
                                        print("Produk ini sudah habis.")
                                else:
                                    print("Produk tidak ditemukan.")

                        elif pilih_user == "2":  # Lihat keranjang
                            if not akun[user_username]['keranjang']:
                                print("Keranjang anda kosong.")
                            else:
                                print("Isi keranjang anda:")
                                for item in akun[user_username]['keranjang']:
                                    print(f"Nama: {item['nama']}, Harga: {item['harga']}")

                        elif pilih_user == "3":  # Edit keranjang
                            if not akun[user_username]['keranjang']:
                                print("Keranjang anda kosong.")
                            else:
                                print("Isi keranjang anda:")
                                for idx, item in enumerate(akun[user_username]['keranjang']):
                                    print(f"{idx + 1}. Nama: {item['nama']}, Harga: {item['harga']}")

                                item_dihapus = input("Masukkan nama produk yang ingin dihapus dari keranjang: ").strip()
                                for item in akun[user_username]['keranjang']:
                                    if item['nama'] == item_dihapus:
                                        akun[user_username]['keranjang'].remove(item)
                                        print(f"Produk {item_dihapus} berhasil dihapus dari keranjang.")
                                        break
                                else:
                                    print("Produk tidak ditemukan di keranjang.")

                        elif pilih_user == "4":  # Checkout
                            total_harga = sum(item['harga'] for item in akun[user_username]['keranjang'])
                            print(f"Total belanja anda: {total_harga}")
                            konfirmasi = input("Apakah anda ingin melanjutkan pembayaran? (yes/no): ").strip().lower()
                            if konfirmasi == 'yes':
                                print("Pembayaran berhasil. Terima kasih telah berbelanja!")
                                akun[user_username]['keranjang'].clear()  # Mengosongkan keranjang setelah checkout
                            else:
                                print("Pembayaran dibatalkan.")

                        elif pilih_user == "5":
                            print("Keluar dari aplikasi.\n")
                            break
                        else:
                            print("Input tidak valid, silakan pilih opsi yang tersedia.\n")

        elif opsi_input == "3":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Input tidak valid, silakan pilih opsi yang tersedia.\n")
