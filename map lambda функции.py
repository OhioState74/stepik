# На вход поступает строка из целых чисел, записанных через пробел. 
# С помощью функции map преобразовать эту строку в список целых чисел,
#  взятых по модулю. Сформируйте именно список lst из таких чисел. 
# Отобразите его на экране в виде набора чисел, идущих через пробел.


print(*list(map(lambda x: abs(int(x)), input().split())))




# Вводится таблица целых чисел. Используя функцию map и генератор списков, преобразуйте 
# список строк lst_in (см. листинг) в двумерный список с именем lst2D, содержащий целые числа. 
# Выводить на экран ничего не нужно, только сформировать список lst2D на основе введенных данных.


import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst2D = list(list(map(int,a.split())) for a in lst_in)



#  На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# True


s = input()
s_lst = s.split()
tp= tuple(tuple(i.split('=')) for i in s_lst)


# (Для учебных целей). Вводится строка. Необходимо в ней заменить кириллические символы на 
# соответствующие латинские обозначения (без учета регистра букв), а все остальные символы - 
# на символ дефиса (-). Для этого в программе определен словарь (см. листинг). Используя его, 
# запишите функцию map, которая бы выдавала преобразованные фрагменты для входной строки. 
# На основе этой функции сформируйте строку, состоящую из преобразованных фрагментов
# (фрагменты в строке должны идти друг за другом без пробелов). Отобразите результат на экране.
# Sample Input:

# Привет Питон
# Sample Output:
# privet-piton


t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', ' ':'-'}


#print(*list(map(t.get, input().lower())), sep = '')

text = input().lower()
trs_text = (t[i] if i in t else '-' for i in text)

for i in trs_text:
    print(i, end='')



# Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию map, которая бы возвращала названия городов только длиной более 5 символов. Вместо остальных названий - строку с дефисом ("-"). Сформировать список из полученных значений и отобразить его на экране в одну строчку через пробел.
# Sample Input:
# Москва Уфа Вологда Тула Владивосток Хабаровск
# Sample Output:
# Москва - Вологда - Владивосток Хабаровск

print(*map(lambda i: i if len(i) >= 5 else '-', input().split()))


s = map(lambda s: s if len(s)>5 else '-', input().split())
print(' '.join(s))

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase
import random
random.seed(1)


def mail_check(mail_len):
    passw = ''
    for char in range(N):
        char=chars[random.randint (0,len(chars)-1)]
        passw+=char
    yield passw + "@mail.ru"

N=int(input())
for i in range(5):
    print(next(mail_check(N)))


#   Определите функцию-генератор, которая бы возвращала простые числа. 
#   (Простое число - это натуральное число, которое делится только на себя и на 1). 
#   Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел. 

def fin_nat_num():
    i=1
    while True:
        i+=1
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            yield i


a = fin_nat_num()
for i in range(20):
    print(next(a), end=' ')


# from sympy import prime


def primes_gen():
    n = 1
    while True:
        yield primes_gen(n)
        n += 1
        
        
gen = primes_gen()

for _ in range(20):
    print(next(gen), end=' ')




def simple_number(n=2):
    
    for number in range(2, 100): 
        if number > 1: 
            for i in range(2, number): 
                if(number % i) == 0: 
                    break 
            else: 
                yield i
       
                

gen=simple_number()
print(*(next(gen) for i in range(20)))       