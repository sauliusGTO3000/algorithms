import array_helper
import random

def binary_to_decimal(binary):
    binaryArray = array_helper.number_to_array(binary)
    binaryArray.reverse()
    i = 0
    decimal = 0
    while i < len(binaryArray):
        decimal += binaryArray[i] * 2**i
        i += 1
    return decimal

def decimal_to_binary(decimal):
    binaryArray = []
    while decimal > 1:
        quotient = decimal / 2
        remainder = decimal % 2
        if remainder < 1:
            binaryArray.append(0)
        else:
            binaryArray.append(1)
        decimal -= quotient
    binaryArray.reverse()
    binaryArray = array_helper.implode_array(binaryArray)
    return binaryArray

number = random.randint(1,999)
numberInBinary = decimal_to_binary(number);
binaryInDecimal = binary_to_decimal(numberInBinary);

print("the number generated: ")
print(number)
print("number in binary:")
print(numberInBinary);
print("number back in decimal:")
print(binaryInDecimal)