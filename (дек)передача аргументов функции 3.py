def strip_excess2(chars='!?'):  #декоратор с начальным параметром


# """
#     Декоратор с параметром "?!:;,. ",  => "-" и "--" или "---" => "-",
#     для функции, меняющей кириллическое написание на латинницу.

#     https://stepik.org/lesson/567063/step/4

#     полный конспект темы:
#     https://github.com/yeralexey/Study/blob/master/stepik.org/decorators.py
# """

    def outer(func):                             # получаем функцию
        def wrapper(string):                     # получаем строку
            d_c = dict.fromkeys(chars, "-")      # словарь из символов в параметре
            result = "".join([d_c[i] if i in d_c else i for i in func(string)])  # замена символов из параметра
            while "--" in result: result = result.replace("--", "-")             # удаление лишних дефисов циклом
            return result
        return wrapper
    return outer

@strip_excess2(chars="?!:;,. ") # аргумент декоратора
def invert_english2(s):         # словарь поместил в функцию, тк. в конспекте есть аналогичный
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    return "".join([t[i] if i in t else i for i in s])  # возвращаем преобразованную строку


# help(strip_excess2)
s = input()                                # ввод с клавиатуры
# s = "Декораторы - это круто!!!!!!!"        # тестовый ввод
print(invert_english2(s.lower()))          # вывод результата функции
