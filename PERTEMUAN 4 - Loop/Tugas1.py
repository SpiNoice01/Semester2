print("")
print("==== PROGRAM SEDERHANA MENGHITUNG JUMLAH TOTAL BILANGAN ==== \n")

A = int(input("Masukkan Bilangan = "))
B = "+ "
sum = 0

for i in reversed(range(1, A+1)):
    if i == 1:
        B = ""
    print(i,B , end="",)
    sum = sum + i
print("=",sum)
print("")
