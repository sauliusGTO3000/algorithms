import random

def random_array(size, lowest = 1, highest = 99):
  i = 0
  array = []
  while i < size:
    array.append(random.randint(lowest,highest))
    i += 1
  return array


def random_binary_number(length):
  binaryArray = []
  i = 0
  while i < length:
    binaryArray.append(random.randint(0,1))
    i += 1
  return binaryArray;

print(random_binary_number(8))