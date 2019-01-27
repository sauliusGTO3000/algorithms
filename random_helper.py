import random

def random_array(size, lowest = 1, highest = 99):
  i = 0
  array = []
  while i < size:
    array.append(random.randint(lowest,highest))
    i += 1
  return array