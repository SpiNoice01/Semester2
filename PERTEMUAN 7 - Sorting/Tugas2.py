def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n ):
            if array[min_idx] > array[j]:
                min_idx = j
                array[i], array[min_idx] = array[min_idx], array[i]
    return array

    
data_array = ["Zhafira", "Nirmala", "Aksara", "Nalendra", "Cakra", "Sastra", "Agni", "Bagas", "Jerome", "Kiara"]
print("Ini Data sebelum di urutkan ",data_array)
data_array.sort()
print("Ini setelah di urutkan", selection_sort(data_array))