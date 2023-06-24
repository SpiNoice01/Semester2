import timeit

def insertion_sort(array):

    start = timeit.default_timer()

    for i in range(1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] < item:
            array[j + 1] =array[j]
            j -= 1
        array[j + 1] = item

    end = timeit.default_timer()
    print(f"Waktu proggram ini di{start - end}")

    return array

data_array = [34,45,67,24,76,12]
print(insertion_sort(data_array))