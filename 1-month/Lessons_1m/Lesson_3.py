"""Операторы: пренадлежности, назначения. Циклы."""

"""Оператор пренадлежности"""

numbers = range(1, 11)
print(7 in numbers)
print(24 in numbers)

word = 'geeks'
print('g' in word)
print('a' in word)

""""Операторы назначения"""

number = 10
print(number)
#number = number + 1 - пример
number += 1 #вместо длинного кода.
number **= 2
number /= 2
number %= 2

print(number)

"""Цикл While"""
"""работает пока проверяемое условие истинно"""

#rounds = 0 #счетчик
#while True: #пока условие цикла True - будет работать до бесконечности.
#    print('Hello, world!', rounds)
#    rounds += 1

#"""from time import sleep #команда для замедленного действия."""

rounds = 0 #счетчик
while rounds <101: #цикл будет работать до 100.
    rounds += 1
#    sleep(0.1) #работает вместе с "from time import sleep"
    if rounds == 51:
        break #прекращает работу цикла

    if rounds == 40:
         continue #игнорирует и продолжает со следущего значения
    if rounds in range(7, 11):
         continue #игнорирует выбранный диапозон и продолжает со следущего значения
    print('Hello world!', rounds)


""" while """
while True:
    time = input('enter time: ').lower()
    if time == 'stop':
        print('stop!')
        break
    if time == 'morning' or time == 'утро':
        print('Good morning')
    elif time == 'day' or time == 'день':
        print('Good day')
    elif time == 'evening' or time == 'вечер':
        print('Good evening')
    elif time == 'night' or time == 'ночь':
        print('Good night')
    else:
        print('Hello')










