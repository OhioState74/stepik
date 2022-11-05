# Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами). 
# Определите декоратор для этой функции, который имеет один параметр tag, определяющий строку с названием тега и начальным значением "h1". Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.

# Пример заключения строки "python" в тег h1: <h1>python</h1>

# Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для введенной строки s:

# s = input()

# Результат отобразите на экране.

# Sample Input:

# Декораторы - это классно!
# Sample Output:

# <div>декораторы - это классно!</div>




def upper_decoration(tag):
    def decoration(func):
        def wraper(*args,**kwargs):
            return (f'<{tag}>{func(*args,**kwargs)}</{tag}>')
        return wraper
    return decoration
    
@upper_decoration(tag="div")
def return_str(s):
    return s.lower()
s=input()
print(return_str(s))









def tag_encloser(tag='h1'):
    return lambda func: lambda *args, **kwards: f'<{tag}>{func(*args, **kwards)}</{tag}>'

@tag_encloser(tag='div')
def make_lower(s):
    return s.lower()

print(make_lower(input()))