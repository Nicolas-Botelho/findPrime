import numpy as np

array = []
for i in range(1, 1000001):
  array.append(i)

def findPrime(arr):
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
  print(findPrime(array))