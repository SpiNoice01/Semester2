def banding(nilai1,nilai2):
    if (nilai1>nilai2):
        print(nilai1)
    elif (nilai1 == nilai2):
        print("Sama")
    else:
        print(nilai2)

bil1 = int(input("Masukan Nilai 1: "))
bil2 = int(input("Masukan Nilai 2: "))

print("bilangan yang lebih besar adalah :", end=" "), banding(bil1, bil2)