# VER. 3.1
# Вариация - добавлена запись в файл


import sys
import time

n = int(input('Диапазон, в котором нужно найти все простые числа, методом перебора, 0 - '))
stdoutOrigin = sys.stdout
sys.stdout = open(f'{n}_prime_numbers.txt', 'a')
start = time.time()
for i in range(7, n + 1):
    counter = 0
    if i % 2 == 0 or i % 5 == 0:
        continue
    for j in range(3, i):
        if i % j == 0:
            counter += 1
        if counter > 0:
            break
    if counter < 1:
        print(i)
end =  time.time()
total_time = end - start
sys.stdout.close()
sys.stdout=stdoutOrigin 
print("Затрачено времени = {}".format(total_time))

