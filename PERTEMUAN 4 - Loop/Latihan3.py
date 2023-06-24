print("==== Mencari Faktor Persekutuan Terbesar \n ")

X = int(input("Masukan Bilangan awal= "))
Y = int(input("Masukan Bilangan kedua= "))

if Y > X :
    bil_terkecil = X 
else :
    X > Y 
    bil_terkecil = Y 
    
for i in range(1, bil_terkecil + 1):
    if(X % i == 0) and (Y % i == 0):
        fpb = i

print("Jadi, Bilangan Dari", X, "Dan", Y, "adalah =", fpb)