buah = [["Apel ", "Jeruk ", "Jambu ", "Anggur ",],
["Nanas ", "Melon ", "Manggis ", "Durian "]]

print(buah ,'\n')

for i in range (buah):
    print(i)

for i in range(len(buah)):
    for j in range (len(buah[i])):
        print(buah[i][j], end="")

