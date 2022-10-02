# №1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def eratosphen(array, num):       #решето Эратосфена
    for i in range(2, num):
        for el in array:
            elem = i**2
            while elem <= num:
                if elem in array:
                    array.remove(elem)
                elem += i
    return array
# prime_nums = eratosphen(list(range(2, N+1)), N)  # простые числа от 2 до N

def factorization(num):     #разложение на множители
    mults = []
    for i in eratosphen(list(range(2, num+1)), num):
        while num % i == 0:
            mults.append(i)
            num /= i
    return mults

# N = 315
# print(f'Множители числа {N}: {factorization(N)}')


# №2. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = 12
b = 45
#использую методы из предыдущей задачи
def nok(num_1, num_2):
    num = max(num_1,num_2)
    prime_nums = eratosphen(list(range(2, num+1)), num)
    if num_1 % num_2 == 0:
        return num_1
    elif num_2 % num_1 == 0:
        return num_2
    elif num_1 in prime_nums or num_2 in prime_nums:
        return num_1*num_2
    else:
        return 'ща подумаем'


# print(f'наименьшее общее кратное {a} и {b} - {nok(a,b)}')

# aa = factorization(a)
# print(f'Множители числа {a}: {aa}')
# bb = factorization(b)
# print(f'Множители числа {b}: {bb}')

# c = aa + bb
# print(c)

# cc = []
# for i in aa:
#     for j in bb:
#         if i == j:
#             cc.append(i)
#             aa.remove(i)
#             bb.remove(i)
#             break
# print('общие множители: ',cc)

#нужно найти пересечение множителей обоих чисел, но методы работы со множествами использовать нельзя
#решение не придумала



# №3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
from random import randint
# n = 13
# my_list = list(randint(0, 10) for i in range(n))
# print(my_list)
# unique = list(set(my_list)) #перевод списка в множество и обратно
# print(unique)


# №4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: # - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# k = 3
# facts = list(randint(0,100) for i in range(k+1))
# print(facts)
# # facts[2] = 0        #для проверки с нулевыми коэффициентами

# polynom_data = open('polynomial.txt', 'w')
# for i in facts:
#     if i != 0:
#         if k == 1:
#             polynom_data.write(str(i) + '*x')
#         if k == 0:
#             polynom_data.write(str(i))
#         if k != 1 and k != 0:
#             polynom_data.write(str(i) + '*x^' + str(k))
#         if i != 0:
#             polynom_data.write(' + ')
#     k -= 1
# polynom_data.write('= 0')
# polynom_data.close()

# with open('polynomial.txt', 'r') as data:
# 	x = data.read()
# with open('polynomial.txt', 'w') as data:
#     x = x.replace(' + = ', ' = ')
#     data.write(x)

# with open('polynomial.txt', 'r') as data:       #вывод в консоль для скрина, что решение работает
#     x = data.read()
#     print(x)


# №5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

#не решена

# with open('polynom_1.txt', 'r') as pol_data_1:
#     pol_1 = pol_data_1.read()
# with open('polynom_2.txt', 'r') as pol_data_2:
#     pol_2 = pol_data_2.read()
# print(pol_1)
# print(pol_2)

# def factors(stroka):
#     for i in stroka.split():
#         print(i)

# factors(pol_2)





# №6. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# d = 0.0001

# sq = 2**(0.5)

# count = 0
# while d < 1:
#     d *= 10
#     count +=1

# sq = round(sq, count)
# print(sq)


