def linear_search(keywords,data):
    for i in range (len(data)):
        if str(data[i]).lower() == keywords.lower():
            print(f"Keyword {keywords} has found at indeks {i}")
            return i
    print(f"Nomor {keywords} Tidak di temukan")
    return -1

data = ["R 2477 SR", "R 1234 DJ", "R 7015 LP", "R 0201 RR", "R 3304 DA", "R 2401 SK", "R 2103 RT", "R 1708 RI", "R 1111 SR", "R 4987 LH"]
keyword = input("Pencari Nomor kendaraan : ")
linear_search(keyword, data)