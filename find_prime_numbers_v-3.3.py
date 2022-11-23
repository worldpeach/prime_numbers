# VER. 3.3
# Улучшения - после первичной проверки есть смысл делить только на нечётные числа. Ускорение почти в два раза по сравнению с предыдущим! Самый быстрый


import time

n = int(input('Диапазон, в котором нужно найти все простые числа, методом перебора, 0 - '))
f = open(f'{n}_prime_numbers.txt', 'a')
start = time.time()
for i in range(1, n + 1):
    counter = 0
    if i % 2 == 0 or i % 5 == 0:
        continue
    for j in range(3, i // 2 + 1, 2):
        if i % j == 0:
            counter += 1
        if counter > 0:
            break
    if counter < 1:
        f.write(str(i)+'\n')
end =  time.time()
total_time = end - start
print("Затрачено времени = {}".format(total_time))
