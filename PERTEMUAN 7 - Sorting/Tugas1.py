def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

data_array = [3.8, 2.9, 3.3, 4.0, 2.7]
print(f"List Sebelum Di urutkan {data_array}")
print("Setelah Diurutkan", bubble_sort(data_array))
