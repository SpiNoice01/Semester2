#Bikin Semacam laman login, tapi pas gagal login ke 3 laman nya tutup
Restart = 0
while True :
    Username = input("Masukan Username : ")
    Password = input("Masukan Password : ")

    if Restart == 2 :
        print("==================== > > > Akun mu ditahan")
        break

    elif Username == "Agil Permana" and Password == "Meong72":
        print("Berhasil Login") 
        break

    else:
        print("Gagal")
        Restart += 1