# VER. 4
# Пытаюсь улучшить - делить на уже открытые простые числа. Проблема в скорости при открытия файла и считывании строк.
# попробовать окрыть файл вначале, чтобы не открывать каждый раз в цикле
# есть такая штука как файловый указатель  tell() seek(). но он работате по байтам, а не по строкам... возможно, не подойдёт.
# делить, естественно, тоже только до половины простых чисел как в алгоритме VER. 3.1

# идея от Юли. Вмозжно итерация проверки деления на 5 лишняя, просто убрать ее из предпроверки, там где проверяется четность. Проверил. Разницы совсем не заметил.

import time
n = int(input('Диапазон, в котором нужно найти все простые числа, методом перебора, 0 - '))
start = time.time()
f = open(f'{n}_prime_numbers.txt', 'a+')
lineNumber = 0 # счётчик найденных простых чисел, он же линий, т.к каждое найденное число в новой строке

# числа до 7 считаем отдельным алгоритмом, без упрощений
if n < 7:
    for i in range(1, n + 1):
        #print('берем', i)
        counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counter += 1

        if counter < 3:
            lineNumber += 1
            #print('найдено простых чисел(и строк в файле) = ', lineNumber)
            f.write(str(j)+'\n')
else:
    f.write('1\n2\n3\n5\n')
    print('1\n2\n3\n5\n записано')
    lineNumber += 4
    #print('lineNumber = ', lineNumber)
f.close()
# этим алгоритмом проверяем по уже существующему списку простых чисел
for i in range(7, n + 1):
    print('проверяем по списку простых чисел:')
    print('берем число', i)
    counter = 0
    if i % 2 == 0 or i % 5 == 0:
        print('число', i, 'пропускаем\n')
        continue
    print('число', i, 'проверяем\n')


    for j in range(2, lineNumber):
        with open(f'{n}_prime_numbers.txt') as f:
            for _ in range(j + 1):
                print('j=',j)
                lineValue = int(f.readline())
                #lineValue = f.readline()
                print('lineValue =',lineValue)
        #lineValue = int(f.readline())
        print('читаем файл построчно')
        print(i, '%', lineValue, 'остаток = ', i % lineValue)
        if i % lineValue == 0:
            counter += 1

        if counter > 0:
            print('о, число', i, 'делится на', lineValue, 'переходим к след числу')
            break
    if counter < 1: # также если counter == 0
        print(i, '- простое. Открываем файл, записываем')
        f.write(str(i)+'\n')
        print('читаем файл построчно')
        lineNumber += 1
        #print('lineNumber = ', lineNumber, ':)')




end =  time.time()
total_time = end - start

f.close()
print("Затрачено времени = {}".format(total_time))
print('результат записан в ', lineNumber, 'линиях')
