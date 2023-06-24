while True:

    print()
    print("1. Penjumblahan \n")
    print("2. Perkalian\n")
    print("3. Pembagian\n")
    print("4. Pengurangan\n")
    print("5. Pemangkatan\n")
    #====================================================================================================#

    Pilih = int(input("Masukan Pilihan : "))
    print("====================================================")
    #=====================================================================================================#

    def nambah(bil1, bil2):
        return (bil1 + bil2)

    def perkalian(bil1, bil2):
        return (bil1 * bil2)

    def pembagian(bil1, bil2):
        return(bil1 / bil2)

    def pengurangan(bil1, bil2):
        return(bil1 - bil2)

    def pemankatan(bil1, bil2):
        return(bil1 ** bil2)
        

    if Pilih == 5:
        Bilangan1 = int(input("Masukan Bilangan Pertama : "))
        Bilangan2 = int(input("Masukan Pangkatnya : "))
    else:
        Bilangan1 = int(input("Masukan Bilangan Pertama : "))
        Bilangan2 = int(input("Masukan Bilangan Kedua : "))
    #===========================================================================================================#

    if Pilih == 1:
        print("Hasil Pertambahannya : ", nambah(Bilangan1, Bilangan2))
    if Pilih == 2:
        print("Hasil Perkalinnya : ", perkalian(Bilangan1, Bilangan2))
    if Pilih == 3:
        print("Hasil Pembagiannya : ", pembagian(Bilangan1, Bilangan2))
    if Pilih == 4:
        print("Hasil Pengurangannya : ", pengurangan(Bilangan1, Bilangan2))
    if Pilih == 5:
        print("Hasil Pemangkatannya : ", pemankatan(Bilangan1, Bilangan2))
    #=============================================================================================================#

    print("========================================================================================================")
    stop = int(input("\nApakan Ingin melakukan Kalkulasi lagi ?\nKetik 1 jika sudah selesai : "))

    if stop == 1:
        break
