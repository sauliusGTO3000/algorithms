def number_to_array(number):
    string = str(number)
    array = []
    for digit in string:
        array.append(int(digit))
    return array

def implode_array(array):
    result = ""
    for element in array:
        result += str(element)
    return result