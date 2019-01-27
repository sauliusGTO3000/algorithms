unsortedList = [1, 2, 7, 4, 75, 10, 58, 221, 4, 32]


def insertion_sort_inc(array):
    j = 1
    while j < (len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i] = key
        j += 1
    return array


def insertion_sort_dec(array):
    j = 1
    while j < (len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] < key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
        j += 1
    return array