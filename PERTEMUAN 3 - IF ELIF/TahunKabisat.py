tahun = int(input("Masukan Tahun : "))

if (tahun %4 == 0) :
    print(tahun, "Adalah Tahun Kabisat")
else :
    print("Ini bukan tahun kabisat")

#Tahun Kabisat adalah 4 tahun sekali, dimana adanya pertamabahan hari.
# Jadi Rumusnya itu, jika tahun bisa habis di bagi terus terusan 4. adalah tahun kabisat.