# VER. 1
# Просто генерирует последовательность чисел, затем каждое сгенерированное пытается делить без остатка на такие же сгенерированные последовательности, без каких либо сокращений своего пути. алгоритм


import time
n = int(input('Диапазон, в котором нужно найти все простые числа, методом перебора, 0 - '))
start = time.time()
for i in range(1, n + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    if counter < 3:
        print(j,end=', ')
end =  time.time()
total_time = end - start
print("Затрачено времени = {}".format(total_time))
