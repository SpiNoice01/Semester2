def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n ):
            if array[min_idx] > array[j]:
                min_idx = j
                array[i], array[min_idx] = array[min_idx], array[i]
    return array

data_array = [90,434,53,56,32,35,23,2]
print(selection_sort(data_array))