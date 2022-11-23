# VER. 2
# Улучшения - алгоритм бросает проверку после первого попавшегося делителя без остатка, кроме 1. Ведь очевидно, что число уже не простое


import time
n = int(input('Диапазон, в котором нужно найти все простые числа, методом перебора, 0 - '))
start = time.time()
for i in range(1, n + 1):
    counter = 0
    for j in range(1, i + 1):
        if counter > 2:
            break
        elif i % j == 0:
            counter += 1
    if counter < 3:
        print(j,end=', ')
end =  time.time()
total_time = end - start
print("Затрачено времени = {}".format(total_time))
