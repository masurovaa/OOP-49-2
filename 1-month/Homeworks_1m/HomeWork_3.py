 #"""Счетчик букв"""

while True:
   command = input('Введите команду "да" или "нет": ').lower()
   glasniye = 'AEUOIYaeuoiyаЯУЮОяуюоеёэиы'
   soglasnie = 'BCDFGHJKLMNPWRSTVWXZbcdfghjklmnpqrstvwxzБВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ'
   letters = ('гласные + согласные')
   if command == 'да':
       word = input('Напишите слово: ')
       print(word)
       counter_glasniy = 0
       for letter in word:
           if letter in glasniye:
            counter_glasniy += 1
            print(letter,counter_glasniy)
       print('Количество гласных букв в слове:',counter_glasniy)
       percent1 = counter_glasniy*100/len(word)

       counter = 0
       print('____________________________')

       for letter in word:
           if letter in soglasnie:
            counter += 1
            print(letter,counter)
       print('Количество согласных букв в слове:',counter)
       percent2 = counter*100/len(word)
       print('____________________________')

       counter = 1
       for letter in word:
          print(letter, counter)
          counter += 1
       print('Количество букв в слове:', int(counter) -1 )
       print('_____________________________')
       print(f"гласные/согласные:{round(percent1,2)}/{round(percent2,2)}%")

   elif command == 'нет':
       print("Выход...")
       break
   else:
       print("Invalid")


