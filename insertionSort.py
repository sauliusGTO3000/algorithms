import random_helper

unsorted_list = random_helper.random_array(9)


def insertion_sort_asc(array):
    j = 1
    while j < (len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
        j += 1
    return array


def insertion_sort_desc(array):
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
