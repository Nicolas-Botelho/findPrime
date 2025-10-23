import numpy as np
import multiprocessing as mp

array = []
for i in range(1, 1000001):
  array.append(i)

n_core: int = 4
part_size: int = len(array) // n_core

def findPrime(arr: list):
  primeList = []

  for num in arr:
    if check_if_prime(num):
      primeList.append(num)

  return primeList

def check_if_prime(num):
  index = 2
  stop = num**0.5 + 1

  if num <= 1:
    return False
  if num == 2:
    return True

  while index < stop:
    if num % index == 0:
      return False
    index += 1
  return True


if __name__ == '__main__':
  array_of_arrays = []

  ant = 0
  for at in range(1, n_core+1):
    array_of_arrays.append(array[(ant*part_size):(at*part_size)])
    ant = at

  pool = mp.Pool(n_core)
  print(pool.map(findPrime, array_of_arrays))