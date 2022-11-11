# Вводятся два списка целых чисел. Необходимо попарно перебрать их элементы и перемножить между собой. При реализации программы используйте функции zip и map. Выведите на экран первые три значения, используя функцию next. Значения выводятся в строчку через пробел. (Полагается, что три выходных значения всегда будут присутствовать).
# Sample Input:
# -7 8 11 -1 3
# 1 2 3 4 5 6 7 8 9 10
# Sample Output:
# -7 16 33


# put your python code here
a=list(map(int,input().split()))
b=list(map(int,input().split()))

lst = [i * j for i, j in zip(a, b)] 
print(*lst[:3]) 
    
       
lst1 = map(int, input().split())
lst2 = map(int, input().split())

lst = map(lambda x, y: x * y, lst1, lst2)
print(*(next(lst) for _ in range(3)))  


#  Вводится неравномерная таблица целых чисел. С помощью функции zip выровнить эту таблицу, приведя ее к прямоугольному виду, отбросив выходящие элементы. Вывести результат на экран в виде такой же таблицы чисел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# sample Input:

# 1 2 3 4 5 6
# 3 4 5 6
# 7 8 9
# 9 7 5 3 2
# Sample Output:

# 1 2 3
# 3 4 5
# 7 8 9
# 9 7 5
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))

for x in zip(*zip(*lst_in)):
   print(*x, sep='')

list(map(print, *zip(*map(str.split, lst_in))))



# Вводится таблица целых чисел. Необходимо сначала эту таблицу представить двумерным списком чисел, а затем, с помощью функции zip выполнить транспонирование этой таблицы (то есть, строки заменить на соответствующие столбцы). Результат вывести на экран в виде таблицы чисел (числа в строках следуют через пробел).
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# 1 2 3 4
# 5 6 7 8
# 9 8 7 6
# Sample Output:
# 1 5 9
# 2 6 8
# 3 7 7
# 4 8 6


import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))



lst_in = [list(map(int, x.split())) for x in lst_in]
res = [list(row) for row in zip(*lst_in)]
for row in res:
   print(*row)

lst_in = map(lambda x: list(map(int, x.split())), lst_in)
for i in list(zip(*lst_in)):
    print(*i)

# Вводится строка из слов, записанных через пробел. Необходимо на их основе составить прямоугольную таблицу из трех столбцов и N строк (число строк столько, сколько получится). Лишнее (выходящее) слово - отбросить. Реализовать эту программу с использованием функции zip. Результат отобразить на экране в виде прямоугольной таблицы из слов, записанных через пробел (в каждой строчке).
# Sample Input:
# Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь
# Sample Output:
# Москва Уфа Тула
# Самара Омск Воронеж
# Владивосток Лондон Калининград


res = zip(*[iter(input().split())]*3)
for x in res:
    print(*x)