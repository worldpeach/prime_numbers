# VER. 3.4
# Улучшения - идея от stepik - у любого составного числа есть делитель (отличный от 1), не превосходящий квадратного корня из числа. Ускорение по сравнению с предыдущей версией - в 89 раз

import time

n = int(input('Диапазон, в котором нужно найти все простые числа, методом перебора, 0 - '))
f = open(f'{n}_prime_numbers.txt', 'a')
start = time.time()
for i in range(1, n + 1):
    counter = 0
    if i % 2 == 0 or i % 5 == 0:
        continue
    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0:
            counter += 1
        if counter > 0:
            break
    if counter < 1:
        f.write(str(i)+'\n')
end =  time.time()
total_time = end - start
print("Затрачено времени = {}".format(total_time))
