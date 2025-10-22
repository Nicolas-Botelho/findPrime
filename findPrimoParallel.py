import numpy as np
import multiprocessing as mp

array = []
for i in range(1, 100001):
  array.append(i)

n_core: int = 4
part_size: int = len(array) // n_core

def findPrimo(arr: list, conn):
  primeList = []

  for num in arr:
    if check_if_prime(num):
      primeList.append(num)

  conn.send(primeList)

  conn.close()

def check_if_prime(num):
  index = 2

  if num <= 1:
    return False

  while index < num:
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

  index = 0
  processes = []
  pipes = []

  while index < n_core:
    p_conn, c_conn = mp.Pipe()
    
    p = mp.Process(
      target=findPrimo,
      args=(array_of_arrays[index],c_conn,)
    )
    
    pipes.append(p_conn)
    processes.append(p)
    
    p.start()
    
    index += 1
  
  result = []

  for p, conn in zip(processes, pipes):
    result.append(conn.recv())
    p.join()
  
  print(result)