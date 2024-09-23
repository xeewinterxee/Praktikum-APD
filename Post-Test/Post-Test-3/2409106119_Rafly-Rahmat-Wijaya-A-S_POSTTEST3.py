# output awalan 
print('''
Kami memilki 3 mobil yang sedang ready, harga ketiga
mobil sama Rp.300.000.000 dengan masing masing diskon yang berbeda
Berikut List Diskon
*******************
* Tesla   = 17%   *
* Toyota  = 21%   *
* Hyundai = 23%   *
*******************
''')

# variabel
nama = str(input("Dengan atas nama siapa? "))
mobil = str(input(f"Baik {nama} ingin membeli mobil apa? "))
harga = int(input(f"Masukkan harga mobil : "))

# kondisi dan output akhiran
if mobil == "tesla":
    diskon_tesla   = harga * 0.17
    hsd_tesla      = harga - diskon_tesla
    print(f"Harga yang harus {nama} bayar : Rp.{hsd_tesla:,.0f}")
elif mobil == "toyota":
    diskon_toyota  = harga * 0.21
    hsd_toyota     = harga - diskon_toyota
    print(f"Harga yang harus {nama} bayar : Rp.{hsd_toyota:,.0f}")
elif mobil == "hyundai":
    diskon_hyundai = harga * 0.23
    hsd_hyundai    = harga - diskon_hyundai
    print(f"Harga yang harus {nama} bayar : Rp.{hsd_hyundai:,.0f}")
else :
    print(f"Terima kasih {nama} telah mengunjungi toko kami")

