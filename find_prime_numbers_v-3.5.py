# VER. 3.5
# Улучшения - вместо счетчика делителей, теперь break и если он не сработал то else для цикла for j.  
# На первом шаге избавился от проверки if i % 2 == 0 or i % 5 == 0:
# вместо i % 2 == 0 цикл с интервалом 2 - for i in range(1, n + 1, 2)

import time

n = int(input('Диапазон, в котором нужно найти все простые числа, методом перебора, 0 - '))
f = open(f'{n}_prime_numbers.txt', 'a')
start = time.time()
for i in range(1, n + 1, 2): 
    #print('test for ', i)
    for j in range(3, int(i ** 0.5) + 1, 2):
        #print('deviding', i, '%', j, '=', i % j)
        if i % j == 0:
            #print('break')
            break # до первого же найденного простого числа.
    else:
        #print('WOW , ',i,'is a prime number')
        f.write(str(i)+'\n')

end = time.time()
total_time = end - start
print("Затрачено времени = {}".format(total_time))
