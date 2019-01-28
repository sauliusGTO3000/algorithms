import array_helper

def binary_to_decimal(binary):
    binary_array = array_helper.number_to_array(binary)
    binary_array.reverse()
    i = 0
    decimal = 0
    while i < len(binary_array):
        decimal += binary_array[i] * 2**i
        i += 1
    return decimal


print(binary_to_decimal(1011110101100001))