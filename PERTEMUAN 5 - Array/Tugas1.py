print()
print()

Lauk = []
Kata = int(input("Masukan Angka, kira-kira ada berapa Lauk Yang Biasanya ada di Padang = "))
Count = 0 #Untuk Menghitung looping dan pertanda stop LOOP

while True:
    Makanan = input("Masukan Nama Lauk = ")
    Lauk.append(Makanan)
    Count += 1
    if Count == Kata:
        break
print(Lauk)

Find = input("\nMasukan Lauk Yang Ingin Di Cari = ")
Isi = Lauk


if Find not in Lauk:
    index = Lauk.index(Find)
    print("Tidak Ada ", index)
else :
    index = Lauk.index(Find) # Data Ada di Index Array Ke Berapa
    print("Lauk Di Temukan, Dan Ada Di Indeks Ke->", index)

print()
print()