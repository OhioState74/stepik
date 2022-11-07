#  Вводится натуральное число N. Необходимо определить функцию-генератор с именем get_sum, которая бы возвращала текущую сумму чисел последовательности длины N в диапазоне целых чисел [1; N]. Например:

# - для первого числа 1 сумма равна 1;
# - для второго числа 2 сумма равна 1+2 = 3
# ....
# - для N-го числа сумма равна 1+2+...+(N-1)+N

# Реализовать функцию-генератор get_sum без использования коллекций. Вызывать ее не нужно, только определить.

# Sample Input:

# 5
# Sample Output:

# 1 3 6 10 15
N = int(input())



def pos(n):
    count = 3
    new_list = [1, 1, 1]
    while count != n:
        lst = new_list[-1] + new_list[-2] + new_list[-3]
        new_list.append(lst)
        count +=1
    return new_list

N = int(input())

print(*pos(N))

# Мы с вами в заданиях несколько раз генерировали последовательность чисел Фибоначчи, которая строится по правилу: каждое последующее число равно сумме двух предыдущих. Для разнообразия давайте будем генерировать каждое последующее как сумму трех предыдущих чисел. При этом первые три числа равны 1 и имеем такую последовательность:

# 1, 1, 1, 3, 5, 9, 17, 31, 57, ...

# Не знаю, есть ли у нее название, поэтому, в рамках уроков, я скромно назову ее последовательностью Балакирева. 

# Итак, на вход программы поступает натуральное число N (N > 5) и необходимо определить функцию-генератор, которая бы возвращала N первых чисел последовательности Балакирева (включая первые три единицы).

# Реализуйте эту функцию без использования коллекций (списков, кортежей, словарей и т.п.). Вызовите ее N раз для получения N чисел и выведите полученные числа на экран в одну строчку через пробел.

# Sample Input:

# 7
# Sample Output:

# 1 1 1 3 5 9 17



def pos(n):
   count = 3
   new_list = [1, 1, 1]
   while count != n:
       lst = new_list[-1] + new_list[-2] + new_list[-3]
       new_list.append(lst)
       count +=1
   return new_list

N = int(input())

print(*pos(N))




def fib():
    f=[]
    while True:
        if len(f)<3:
            f.append(1)
            yield 1
        else:
            res= f[-1]+f[-2]+f[-3]
            f.append(res)
            yield res
t = fib()
for _ in range(int(input())):
    print(next(t), end=' ')


# Вводится натуральное число N (N > 8). Необходимо определить функцию-генератор, которая бы выдавала пароль длиной N символов из случайных букв, цифр и некоторых других знаков. Для получения последовательности допустимых символов для генерации паролей в программе импортированы две строки: ascii_lowercase, ascii_uppercase (см. листинг ниже), на основе которых формируется общий список:

# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной N и делать это бесконечно, то есть, вызывать ее можно бесконечное число раз. Сгенерировать случайный индекс indx в диапазоне [a; b] для символа можно с помощью функции randint модуля random:

# import random
# random.seed(1)
# indx = random.randint(a, b)
# Сгенерируйте с помощью этой функции первые пять паролей и выведите их в столбик (каждый с новой строки).

# Sample Input:

# 10
# Sample Output:

# riGp?58WAm
# !dX3a5IDnO
# dcdbWB2d*C
# 4?DSDC6Lc1
# mxLpQ@2@yM

import random
from string import ascii_lowercase, ascii_uppercase

# установка зерна датчика случайных чисел (не менять)
random.seed(1)

# здесь продолжайте программу
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

def password_check(password_len):
    passw = ''
    for char in range(N):
        char=chars[random.randint (0,len(chars))]
        passw+=char
    yield passw

N=int(input())
for i in range(5):
    print(next(password_check(N)))

#   Вводится натуральное число N. Используя строки из латинских букв ascii_lowercase и ascii_uppercase:

# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase
# задайте функцию-генератор, которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и длиной в N символов. Например, при N=6, получим адрес: SCrUZo@mail.ru

# Для формирования случайного индекса для строки chars используйте функцию randint модуля random:

# import random
# random.seed(1)
# indx = random.randint(0, len(chars)-1)
# Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно. Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).

# Sample Input:

# 8
# Sample Output:

# iKZWeqhF@mail.ru
# WCEPyYng@mail.ru
# FbyBMWXa@mail.ru
# SCrUZoLg@mail.ru
# ubbbPIay@mail.ru   

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


from sympy import prime


def primes_gen():
    n = 1
    while True:
        yield prime(n)
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