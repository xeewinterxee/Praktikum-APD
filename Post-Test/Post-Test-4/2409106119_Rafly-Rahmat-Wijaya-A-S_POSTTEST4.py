print('''
    *SELAMAT DATANG DI APLIKASI HALOMOBIL*
Silahkan login terlebih dahulu
1.Login
2.Keluar''')

opsi = input("Masukkan nomor opsi : ")

if opsi == "1":
    nama      = 'rafly'
    nim       = '119'
    percobaan = 0
else:
    print("Terima kasih telah mengunjungi aplikasi kami")
    exit()

while (percobaan < 3):
    username   = input("Masukkan Username : ")
    password   = input("Masukkan Password : ")
    percobaan += 1
    kesempatan_percobaan = 3 - percobaan

    if username == nama and password == nim :
        print("Anda berhasil login")
        break
    elif kesempatan_percobaan > 0 :
        print(f"login gagal, kesempatan login tersisa {kesempatan_percobaan}")
    else: 
        print("login gagal, Maaf sesi login anda sudah habis")
        exit()

print('''
**** MERK MOBIL ****
* 1.Mobil Tesla    *
* 2.Mobil Toyota   *
* 3.Mobil Hyundai  *
********************''')

while True:
    mobil = input("Masukkan angka mobil yang anda pilih :")
    if mobil == '1':
        print("Anda memilih Mobil Tesla.")
        break
    elif mobil == '2':
        print("Anda memilih Mobil Toyota.")
        break
    elif mobil == '3':
        print("Anda memilih Mobil Hyundai.")
        break
    else:
        print("Mobil tidak tersedia")