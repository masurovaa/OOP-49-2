print('hello world')
# Список расходов за каждый день недели и подсчет среднего расхода
day1 = float(input('Введите расход за понедельник:'))
day2 = float(input('Введите расход за вторник:'))
day3 = float(input('Введите расход за среду:'))
day4 = float(input('Введите расход за четверг:'))
day5 = float(input('Введите расход за пятницу:'))
day6 = float(input('Введите расход за субботу:'))
day7 = float(input('Введите расход за воскресенье:'))

summ = day1 + day2 + day3 + day4 + day5 + day6 + day7
print("Общая сумма расходов", summ, "сомов")

average = summ/7
average_round = round(average, 1)
print('Средняя сумма расходов за неделю', average_round, 'сомов')






