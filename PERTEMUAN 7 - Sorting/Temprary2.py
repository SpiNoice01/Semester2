def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

data_array = [45,5,45,56,999,554,55]
print(bubble_sort(data_array))