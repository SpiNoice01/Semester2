print("============= Menghitung Pangkat")

duaawal = int(input("Masukan 2 angka nim awal mu = "))
duaakhir = int(input("Masukan 1 atau 2 Angka Nim Akhirmu = "))

jumlahdua = duaawal + duaakhir
kali2 = jumlahdua * jumlahdua

pangkat = int(input("Masukan Pencacah = "))

for i in range(1, pangkat+1):
    akhir = (kali2 * i)

    print(f"Pemangkatan2 ke {i} = ", akhir)
