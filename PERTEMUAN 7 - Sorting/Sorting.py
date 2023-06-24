import timeit
print(" ")
print(" ")
print("Ascending")
print(" ")

#insertion Sort
def insertion_sort(array):
    start = timeit.default_timer()
    for i in range(1, len(array)):
        item = array [i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1

            array [j + i] = item

        stop = timeit.default_timer()
        print(f"Insertion Sort Sucsessful! Elapsed Time : + {stop - start}")
        return array

list_1 = [133, 21, 35, 74, 58, 64, 73, 86, 39, 10]
print(f"Before: {list_1}")
insertion_sort(list_1)
print(f"After: {list_1}")

# bubble sorting
def bubble_sort(array):
    start = timeit.default_timer()
    for i in range (len(array)):
        for j in range (len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    
    stop = timeit.default_timer()
    print(f"Bubble Sort Sucsessful! Elapsed time {stop - start}")
    return array

print(bubble_sort([7,1,5,0,10]))