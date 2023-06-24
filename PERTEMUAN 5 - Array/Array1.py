angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
angka2 = ["Satu ", "Dua ", "Tiga ", "Empat ", "Lima "]


a = angka2[3]
print(a)

print(angka)
print(angka2)

angka2.append("Enam")
print(angka2)

angka2[1] = "Sepuluh "
print(angka2)

print("len ", end="")
panjang = len(angka2)
print(panjang,)

for i in angka2:
    print(i)

angka2.pop(2)
angka2.remove("Satu ")
print(angka2)