print("========= KPK =======")

Bilangan1 = int(input("Masukan Bilangan pertama = "))
Bilangan2 = int(input("Masukan Bilangan Kedua = "))

a = Bilangan1
b = Bilangan2

while a != b:
    if a > b:
        b = Bilangan2 + b
    else:
        a = Bilangan1 + a

print("KPK Nya adalah = ", a)
