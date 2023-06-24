#Menambah data mahasiswa
def Tambahsiswa():
    jumlah = int(input("Jumlah Mahasiswa: "))
    mahasiswa = []
    while(jumlah > 0 ):
        nama = input("Nama Mahasiswa: ")
        mahasiswa.append(nama)
        jumlah = jumlah - 1
    
    while (True):
        panggil(mahasiswa)
        jumlah = jumlah - 1
        if(jumlah<0):
            break

#Hapus data mahasiswa
def hapus_siswa(arrayMahasiswa):
    mahasiswa = arrayMahasiswa
    print("Data Mahasiswa %s" %arrayMahasiswa)
    mahasiswa.remove(input("Hapus Mahasiswa: " , "\n(Tolong Perhatikan, Kapital, Dan tanda baca lainnya.)"))
    print("Data mahasiswa %s" %mahasiswa)
    panggil(mahasiswa)

#Urutkan data mahasiswa
def sort_Mahasiswa(arrayMahasiswa):
    mahasiswa = arrayMahasiswa
    mahasiswa.sort()
    print(mahasiswa)
    panggil(mahasiswa)

#Lihat Data mahasiswa
def LiatSiswa(arrayMahasiswa):
    mahasiswa = arrayMahasiswa
    for x in mahasiswa:
        print("Nama Mahasiswa: %s" %x)
    panggil(mahasiswa)

#Menu
def panggil(arrayMahasiswa):
    print("\n<========================================== Menu Data Mahasiswa|")
    print("1. Tambah Data Mahasiswa ")
    print("2. Hapus Data Mahasiswa ")
    print("3. Urutkan Data Mahasiswa ")
    print("4. Lihat Data Mahasiswa ")
    print("5. Tutup")

    pilih = int(input("Pilihan : "))
    
    if pilih == 1:
        Tambahsiswa()
    elif pilih == 2:
        hapus_siswa(arrayMahasiswa)
    elif pilih == 3:
        sort_Mahasiswa(arrayMahasiswa)
    elif pilih == 4:
        LiatSiswa(arrayMahasiswa)
    else:
        print("Selesai")

Tambahsiswa()