# На вход программы поступает строка из целых чисел, записанных через пробел. Напишите функцию get_list, которая преобразовывает эту строку в список из целых чисел и возвращает его. Определите декоратор для этой функции, который сортирует список чисел по возрастанию. Результат сортировки должен возвращаться при вызове декоратора.

# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:

# print(*lst)

# Sample Input:

# 8 11 -5 4 3 10
# Sample Output:

# -5 3 4 8 10 11







def sort_numbers(func):
    def wrapper(*args, **kwargs):
        return sorted(func(*args, **kwargs))
    return wrapper


@sort_numbers
def get_list(line):
    return map(int, line.split())


lst = get_list(input())
print(*lst)










def check_num(func):
    def wrapper(*args,**kwargs):
        return sorted (func(*args, **kwargs))
        
    return wrapper   
        
    
@check_num
def get_list(numbers):
    numbers = list(map(int, numbers.split()))
    return numbers

    
lst = get_list(input())
print(*lst)  