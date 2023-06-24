print()
print()

Nilai = []
Matkul = int(input("Masukan Jumlah Mata Kuliah = "))
Counter = 0


while True:
    Nilai_i = int(input(f"Masukan Nilai Matkul Kuliah ke- {Counter+1} : ")) #Tempat Kita Masukin Nilai
    Nilai.append(Nilai_i)
    Counter += 1
    if Counter == Matkul:
        break
    else:
        if Nilai_i > 101 :
            break

Sum = sum(Nilai)
Avg = (Sum / Matkul)
print("")

if Avg > 100:
    print("!!!!! Error Nilai Di Atas 100 !!!!!!")
elif Avg >= 90 <= 100:
    print("Predikat Mu = A")
    print("Nilai Rata-Rata Mu =", Avg)
elif Avg >= 70 <= 90:
    print("Predikat Mu = B")
    print("Nilai Rata-Rata Mu =", Avg)
elif Avg >= 50 <= 70:
    print("Predikat Mu = C")
    print("Nilai Rata-Rata Mu =", Avg)
elif Avg >= 30 <= 50:
    print("Predikat Mu = D")
    print("Nilai Rata-Rata Mu =", Avg)
else :
    print("Predikat Mu = E")
    print("Nilai Rata-Rata Mu =", Avg)

print("")
print("")