
# Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список чисел и возвращает их сумму.

# Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:

# s = input()

# Результат отобразите на экране.

# Sample Input:

# 5 6 3 6 -4 6 -1
# Sample Output:

# 26











def num_start(start=5):
    def num_str(func):
        def wrapper(*args,**kwargs):
            res=func(*args,**kwargs)
            res=res+start
            return res
        return wrapper
    return num_str

@num_start(start=5)
def num_sum(string):
    return sum(list(map(int,string.split())))

s = input()
print(num_sum(s))