# Задача 1. Дано натуральное число N.
# Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396

def chisla():
    n = input('Введите число: ')
    m = int(input('Введите количество преобразований числа: '))    
    summ = 0
    for i in range(1, m + 1):
        num = n * i
        print(num)
        summ = (summ+int(num))
    print(summ)

# Задача 2. Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число.
# Напишите программу, которая определяет, есть в массиве
# последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

def massiv():
    massiv = [random.randint(0, 9) for _ in range(15)]
    print(massiv)
    number = input('Введите число: ')

    res = []
    for el in number:
        res.append(int(el))

    result = False
    for i in range(len(massiv) - len(res)):
        if res == massiv[i:len(res) + i]:
            result = True

    if result == True:
        print(f'{massiv} - {res} -> да')
    else:
        print(f'{massiv} - {res} -> нет')

# Задача 3. Найдите все простые несократимые дроби,
# лежащие между 0 и 1, знаменатель которых не превышает 11.

def drobi():
    n = 1
    while n < 11: 
        m = 2       
        while m <= 11:
            if m / n > 1:
                if n == 1:
                    print(f'{n}/{m}') 
                if m % n != 0:
                    if n > 2 and n % 2 == 0 and m % 2 != 0:
                        print(f'{n}/{m}')
                    if n == 2 and m % 2 != 0:
                        print(f'{n}/{m}') 
                    if n % 2 == 1:
                        print(f'{n}/{m}') 
            m += 1
        n += 1
