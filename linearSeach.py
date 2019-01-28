import random_helper

array = random_helper.random_array(58,1,99)


def linear_search(haystack, needle):
    i = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return haystack.index(needle)
        i += 1
    return


print(linear_search(array, 5))
