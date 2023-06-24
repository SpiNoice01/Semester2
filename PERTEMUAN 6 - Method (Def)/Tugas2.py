while True :

    def keliling_lingkaran(jari):
        return 2 * (22/7 * jari)
    def luas_lingkaran(diameterr):
        return 22/7 * diameterr

    jari_jari = int(input("Masukan Jari-jari nya : "))
    diameter = jari_jari * 2

    print("Keliling Lingkaran Nya adalah : %f " % keliling_lingkaran(jari_jari))
    print("Luas Lingkaran Nya Adalah : %f" % luas_lingkaran(diameter))

    kesepakatan = int(input("Ketik 1 jika ulang dan 2 jika selesai = "))
    if kesepakatan == 2:
        break 