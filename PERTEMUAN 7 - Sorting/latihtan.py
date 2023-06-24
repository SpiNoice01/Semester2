def addMahasiswa():
    jumlah = int(input("jumlah Mahasiswa: "))
    mahasiswa = []
    while(jumlah > 0):
        nama = input("Nama Mahasiswa: ")
        mahasiswa.append(nama)
        jumlah = jumlah - 1
    
    while True:
        panggil(mahasiswa)
        jumlah = jumlah - 1
        if(jumlah < 0):
            break
    
def removeMahasiswa(arrayMahasiswa):
    mahasiswa = arrayMahasiswa
    print("Data mahasiswa %s" %arrayMahasiswa)
    mahasiswa.remove(input("Hapus Mahasiswa: "))
    print("Data Mahasiswa %s" %mahasiswa)
    panggil(mahasiswa)

def ascMahasiswa(arrayMahasiswa):
    mahasiswa = arrayMahasiswa
    mahasiswa.sort()
    print(mahasiswa)
    panggil(mahasiswa)

def viewMahasiswa(arrayMahasiswa):
    mahasiswa = arrayMahasiswa
    for x in mahasiswa:
        print("Nama Mahasiswa: %s" %x)
    panggil(arrayMahasiswa)

def panggil(arrayMahasiswa):
    print("<============================== Menu Data Mahasiswa |")
    print("1. Tambah Mahasiswa")
    print("2. Hapus Mahasiswa, Yang di tambahkan")
    print("3. Urutkan Mahasiswa, Yang di tambahkan")
    print("4. Lihat Mahasiswa, Yang di tambahkan")
    print("5. Tutup (Selesai), Yang di tambahkan")

    pilih = int(input("Masukan Pilihan: "))

    if pilih == 1:
        addMahasiswa()
    elif pilih == 2:
        removeMahasiswa(arrayMahasiswa)
    elif pilih == 3:
        ascMahasiswa(arrayMahasiswa)
    elif pilih ==4 :
        viewMahasiswa(arrayMahasiswa)
    else:
        print("Selesai")

addMahasiswa()