akun = []
daftar_produk = []

while True:
    print("Selamat datang di TOKOSHOPI")
    print("=== Selamat datang di TOKOSHOPI ===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")         

    # input
    opsi_input = input("Pilih opsi? (1/2/3): ").strip()
    print("")

    # cek input tidak boleh kosong
    if not opsi_input:
        print("Input tidak boleh kosong. Silakan masukkan 1, 2, atau 3.\n")

    # cek input harus angka
    elif not opsi_input.isdigit():
        print("Input harus berupa angka. Silakan masukkan 1, 2, atau 3.\n")

    # cek input dalam rentang 1,2,3
    elif opsi_input not in ["1", "2", "3"]:
        print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.\n")

    else:
        # register
        if opsi_input == "1":
            print("Silahkan pilih role")
            print("1.admin")
            print("2.user")
            regis_input = input("Pilih role anda?(1/2):")
            print("")

            # admin
            if regis_input == "1":
                admin_username = input("Masukkan username:")
                admin_cek = False
                for admin_akun in akun :
                    if admin_akun[0] == admin_username:
                        admin_cek = True
                        break
                if admin_cek:
                    print("Username telah dipakai")
                else:
                    admin_password = input("Masukkan password:")
                    akun.append([admin_username, admin_password, []])
                    print("Akun admin anda telah terdaftar")

            # user
            elif regis_input == "2":
                user_username = input("Masukkan username:")
                user_cek = False

                for user_akun in akun:
                    if user_akun[0] == user_username:
                        user_cek = True
                        break
                if user_cek:
                    print("Username telah dipakai")
                else:
                    user_password = input("Masukkan password:")
                    akun.append([user_username, user_password, []])
                    print("Akun user anda telah terdaftar")
            else:
                # print("Input tidak valid")
                # # cek input tidak boleh kosong
                # cek input tidak boleh kosong
                if not regis_input:
                    print("Input tidak boleh kosong. Silakan masukkan 1, 2, atau 3.\n")

                # cek input harus angka
                elif not regis_input.isdigit():
                    print("Input harus berupa angka. Silakan masukkan 1, 2, atau 3.\n")

                # cek input dalam rentang 1,2,3
                elif regis_input not in ["1", "2", "3"]:
                    print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.\n")

        # login
        elif opsi_input == "2":
            print("Pilih akun anda")
            print("1.admin")
            print("2.user")
            login_input = input("Pilih role anda:")

            # login admin
            if login_input == "1":
                admin_username = input("Masukkan username:")
                admin_password = input("Masukkan password:")
                for admin_akun in akun:
                    if admin_akun[0] == admin_username and admin_akun[1] == admin_password:
                        while True:
                            print(f"\nSelamat datang {admin_username}!")
                            print("―――Silakan pilih aksi!―――")
                            print("1. Menambah produk ")
                            print("2. Melihat produk  ")
                            print("3. Edit/ubah produk")
                            print("4. Hapus produk")
                            print("5. Exit")
                            print("―――――――――――――――――――――――――――――")

                            pilih = input("Pilih opsi: ")
                            print(" ")

                            # tambah produk
                            if pilih == "1":
                                nama_produk = input("Masukkan nama produk: ").strip()
                                deskripsi_produk = input("Masukkan deskripsi produk: ").strip()
                                stok_produk = input("Masukkan stok produk: ").strip()
                                harga_produk = input("Masukkan harga produk: ").strip()

                                if not nama_produk or not deskripsi_produk or not stok_produk or not harga_produk:
                                    print("Semua data produk harus diisi.")
                                elif not stok_produk.isdigit() or not harga_produk.isdigit():
                                    print("Stok dan harga harus berupa angka.")
                                else:
                                    daftar_produk.append([nama_produk, deskripsi_produk, int(stok_produk), int(harga_produk)])
                                    print("Produk berhasil ditambahkan.")


                            # lihat produk
                            elif pilih == "2":
                                    if not daftar_produk:
                                        print("Tidak ada produk yang tersedia saat ini.")
                                    else:
                                        print("Daftar produk yang tersedia:")
                                        for indeks, produk in enumerate(daftar_produk):
                                            print(f"{indeks + 1}. Nama: {produk[0]}, Deskripsi: {produk[1]}, Stok: {produk[2]}, Harga: {produk[3]}\n")
                            # edit produk
                            elif pilih == "3":
                                if not admin_akun[2]:
                                    print("Tidak ada produk untuk diedit.\n")
                                else:
                                    # Meminta input nomor produk, dengan pengecekan apakah input berupa angka
                                    input_edit = input("Masukkan nomor produk yang ingin diedit: ").strip()

                                    # Cek apakah input kosong
                                    if not input_edit:
                                        print("Nomor produk tidak boleh kosong.\n")

                                    # Cek apakah input berupa angka
                                    elif not input_edit.isdigit():
                                        print("Nomor produk harus berupa angka.\n")

                                    else:
                                        indeks_produk = int(input_edit) - 1

                                        # Cek apakah nomor produk valid (ada dalam daftar produk)
                                        if 0 <= indeks_produk < len(admin_akun[2]):
                                            print(f"Produk yang akan diedit: {admin_akun[2][indeks_produk]}")

                                            # Meminta input perubahan dengan pengecekan input kosong
                                            nama_baru = input("Masukkan nama baru (atau tekan Enter untuk tidak mengubah): ").strip()
                                            deskripsi_baru = input("Masukkan deskripsi baru (atau tekan Enter untuk tidak mengubah): ").strip()
                                            stok_baru = input("Masukkan stok baru (atau tekan Enter untuk tidak mengubah): ").strip()
                                            harga_baru = input("Masukkan harga baru (atau tekan Enter untuk tidak mengubah): ").strip()

                                            # Cek dan perbarui hanya jika input tidak kosong
                                            if nama_baru:
                                                admin_akun[2][indeks_produk][0] = nama_baru
                                            if deskripsi_baru:
                                                admin_akun[2][indeks_produk][1] = deskripsi_baru

                                            # Cek apakah stok dan harga yang dimasukkan adalah angka
                                            if stok_baru:
                                                if stok_baru.isdigit():
                                                    admin_akun[2][indeks_produk][2] = int(stok_baru)
                                                else:
                                                    print("Stok harus berupa angka.\n")

                                            if harga_baru:
                                                if harga_baru.isdigit():
                                                    admin_akun[2][indeks_produk][3] = int(harga_baru)
                                                else:
                                                    print("Harga harus berupa angka.\n")

                                            print("Produk berhasil diedit.\n")

                                        else:
                                            print("Produk tidak ditemukan.\n")

                            
                            # hapus produk
                            elif pilih == "4":
                                if not admin_akun[2]:
                                    print("Tidak ada produk untuk dihapus.\n")
                                else:
                                    input_hapus = input("Masukkan nomor produk yang ingin dihapus: ").strip()

                                    # Cek apakah input kosong
                                    if not input_hapus:
                                        print("Nomor produk tidak boleh kosong.\n")

                                    # Cek apakah input berupa angka
                                    elif not input_hapus.isdigit():
                                        print("Nomor produk harus berupa angka.\n")

                                    else:
                                        indeks_hapus = int(input_hapus) - 1

                                        # Cek apakah nomor produk valid
                                        if 0 <= indeks_hapus < len(admin_akun[2]):
                                            admin_akun[2].pop(indeks_hapus)
                                            print("Produk berhasil dihapus.\n")
                                        else:
                                            print("Produk tidak ditemukan.\n")


                            # Keluar dari Menu Admin
                            elif pilih == "5":
                                print("Keluar dari aplikasi.\n")
                                break

                            else:
                                print("Input tidak valid, silakan pilih opsi yang tersedia.\n")

            # login user
            elif login_input == "2":
                user_username = input("Masukkan username: ")
                user_password = input("Masukkan password: ")
                for user_akun in akun:
                    if user_akun[0] == user_username and user_akun[1] == user_password:
                        print(f"\nSelamat datang {user_username}!")
                        
                        # Tampilkan daftar produk setelah login
                        if not daftar_produk:
                            print("Tidak ada produk yang tersedia saat ini.")
                        else:
                            print("Daftar produk yang tersedia:")
                            for indeks, produk in enumerate(daftar_produk):
                                print(f"{indeks + 1}. Nama: {produk[0]}, Deskripsi: {produk[1]}, Stok: {produk[2]}, Harga: {produk[3]}\n")
                        
                        # Setelah menampilkan produk, masuk ke menu pilihan user
                        while True:
                            print("―――Silakan pilih aksi!―――")
                            print("1. Tambah produk yang ingin dibeli ")
                            print("2. Melihat keranjang belanja  ")
                            print("3. Edit/ubah produk belanja")
                            print("4. Hapus produk belanja")
                            print("5. Exit")
                            print("―――――――――――――――――――――――――――――")

                            pilih = input("Pilih opsi: ")
                            print(" ")

                            if pilih == "1":
                                # Menambah produk ke keranjang belanja
                                produk_yang_ingin_dibeli = input("Masukkan nama produk yang ingin dibeli: ").strip()
                                user_akun[3].append(produk_yang_ingin_dibeli)  # Menambahkan produk ke keranjang
                                print(f"{produk_yang_ingin_dibeli} berhasil ditambahkan ke keranjang belanja.")

                            elif pilih == "2":
                                # Melihat keranjang belanja
                                if not user_akun[3]:
                                    print("Keranjang belanja Anda kosong.")
                                else:
                                    print("Produk dalam keranjang belanja:")
                                    for indeks, produk in enumerate(user_akun[3]):
                                        print(f"{indeks + 1}. {produk}")

                            elif pilih == "3":
                                # Mengedit produk dalam keranjang belanja
                                if not user_akun[3]:
                                    print("Tidak ada produk dalam keranjang belanja untuk diedit.")
                                else:
                                    print("Produk dalam keranjang belanja:")
                                    for indeks, produk in enumerate(user_akun[3]):
                                        print(f"{indeks + 1}. {produk}")

                                    produk_edit = int(input("Masukkan nomor produk yang ingin diubah: ")) - 1
                                    if 0 <= produk_edit < len(user_akun[3]):
                                        produk_baru = input("Masukkan nama produk baru: ").strip()
                                        user_akun[3][produk_edit] = produk_baru  # Mengganti produk lama dengan yang baru
                                        print("Produk berhasil diubah.")
                                    else:
                                        print("Nomor produk tidak valid.")

                            elif pilih == "4":
                                # Menghapus produk dari keranjang belanja
                                if not user_akun[3]:
                                    print("Tidak ada produk dalam keranjang belanja untuk dihapus.")
                                else:
                                    print("Produk dalam keranjang belanja:")
                                    for indeks, produk in enumerate(user_akun[3]):
                                        print(f"{indeks + 1}. {produk}")

                                    produk_hapus = int(input("Masukkan nomor produk yang ingin dihapus: ")) - 1
                                    if 0 <= produk_hapus < len(user_akun[3]):
                                        del user_akun[3][produk_hapus]  # Menghapus produk dari keranjang
                                        print("Produk berhasil dihapus dari keranjang belanja.")
                                    else:
                                        print("Nomor produk tidak valid.")

                            elif pilih == "5":
                                print("Terima kasih, Anda telah keluar.")
                                break  # Keluar dari loop user
            else:
                # cek input tidak boleh kosong
                if not login_input:
                    print("Input tidak boleh kosong. Silakan masukkan 1 atau 2.\n")

                # cek input harus angka
                elif not login_input.isdigit():
                    print("Input harus berupa angka. Silakan masukkan 1 atau 2.\n")

                # cek input dalam rentang 1,2,3
                elif login_input not in ["1", "2"]:
                    print("Pilihan tidak valid. Silakan masukkan 1 atau 2.\n")
        
        elif opsi_input == "3":
                print("Terima kasih telah mengunjungi aplikasi kami")
                break
        else:
            print("input tidak valid")