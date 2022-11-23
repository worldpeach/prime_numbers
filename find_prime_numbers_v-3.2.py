# VER. 3.2
# Улучшения - Проверяем только до половины делителей!


import time

n = int(input('Диапазон, в котором нужно найти все простые числа, методом перебора, 0 - '))
f = open(f'{n}_prime_numbers.txt', 'a')
start = time.time()
for i in range(7, n + 1):
    counter = 0
    if i % 2 == 0 or i % 5 == 0:
        continue
    for j in range(3, i // 2 + 1):
        if i % j == 0:
            counter += 1
        if counter > 0:
            break
    if counter < 1:
        f.write(str(i)+'\n')
        #print(i)
        #print(i,end=', ')
end =  time.time()
total_time = end - start
print("Затрачено времени = {}".format(total_time))
