"""Функции: виды параметров. возвращенние данных. виды аргументов."""
# DRY - don't repeat yourself
# def - define. Определить
# параметры - указываются при создании функции

"""Схема функции"""
"""определение функции -> наименование функции -> (параметры):
(тело к функции)
возвращение данных

вызов функции
наименование (аргументы)"""

""" Функция создается с помощью ключевого слова - 'def' """
#def name_function(): #определение функции
#    print('hello world') #тело

#name_function() #вызов функции
#name_function()
#name_function()

#def name_function(name): #required positional argument - обязательный параметр
#   print(f'hello {name}')

# name_function() #required positional argument нужен
""" аргументы - передается при вызове функции"""
#name_function('Altynai')

"""Виды параметров"""
"""параметры по умолчанию"""
#def name_function(name='неизвестно'): #name - необязательный параметр
#    print(f'hello {name}')

#name_function()
#name_function('Tilek')

#def name_function(surname, name='неизвестно'): #surname - обязательный параметр
#    print(f'фамилия: {surname} имя: {name}')
"""keyword arguments - ключевые аргументы"""
#name_function(name='Altynai', surname='Masurova')

#length = 7
#width = 5
#square_2 = length * width
#print(square_2)

#length = 300
#width = 150
#square_victory = length * width
#print(square_victory)

#def get_square(length, wigth):
#    return length * wigth
#square_2 = get_square(7, 5)
#square_victory = get_square(300, 150)

#print(square_2)
#print(square_victory)