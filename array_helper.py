def number_to_array(number):
    string = str(number)
    array = []
    for digit in string:
        array.append(int(digit))
    return array