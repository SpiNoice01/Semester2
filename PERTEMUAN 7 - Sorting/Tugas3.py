################################################################################## list bukuan

print()
print()

Judul = []
JudulD = []
Jumlbuku = int(input("Masukan Total Buku = "))
Count = 0 #Untuk Menghitung looping dan pertanda stop LOOP

while True:
    Buku = input("Masukan Nama Judul= ")
    Judul.append(Buku)
    JudulD.append(Buku)
    Count += 1
    if Count == Jumlbuku:
        break



print()
print()

##################################################################################
##====================================== Insertion Sort Ascending

def insertion_sort(array):

    for i in range(1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array[j + 1] =array[j]
            j -= 1
        array[j + 1] = item


    return array

##==================================== Insertion Sort Descendin

def insertion_sortD(array):

    for i in range(1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] < item:
            array[j + 1] =array[j]
            j -= 1
        array[j + 1] = item


    return array

#######################################################################################
##============================================ Choose

a = (insertion_sort(Judul))
b = (insertion_sortD(JudulD))

print("<===================== Urutkan ? ")
print("1. insertion_Ascending")
print("2. Insertion_Descending")
pilihan = int(input("> > > Pilihan Mu :"))
print()

if pilihan == 1:
    for urut in range(0, len(a)):####
        print(f"Judul Buku Ke - {urut+1}", a[urut])####
else :
    for urut in range(0, len(b)):####
        print(f"Judul Buku Ke - {urut+1}", b[urut])####
