

day = input('Введите дату рождения: ').lower()
month = input('Введите месяц рождения (цифрами): ').lower()

if(month == '3' and day >= '21' and day <= '31') or (month == '4' and day >= '1' and day <= '20'):
    print("Ваш знак зодиака: Овен")
elif(month == '4' and day >= '21' and day <= '30') or (month == '5' and day >= '1' and day <= '21'):
    print("Ваш знак зодиака: Телец")
elif(month == '5' and day >= '22' and day <= '31') or (month == '6' and day >= '1' and day <= '21'):
    print("Ваш знак зодиака: Близнецы")
elif(month == '6' and day >= '22' and day <= '30') or (month == '7' and day >= '1' and day <= '22'):
    print("Ваш знак зодиака: Рак")
elif(month == '7' and day >= '23' and day <= '31') or (month == '8' and day >= '1' and day <= '21'):
    print("Ваш знак зодиака: Лев")
elif(month == '8' and day >= '22' and day <= '31') or (month == '9' and day >= '1' and day <= '23'):
    print("Ваш знак зодиака: Дева")
elif(month == '9' and day >= '24' and day <= '30') or (month == '10' and day >= '1' and day <= '23'):
    print("Ваш знак зодиака: Весы")
elif(month == '10' and day >= '24' and day <= '31') or (month == '11' and day >= '1' and day <= '22'):
    print("Ваш знак зодиака: Скорпион")
elif(month == '11' and day >= '23' and day <= '30') or (month == '12' and day >= '1' and day <= '22'):
    print("Ваш знак зодиака: Стрелец")
elif(month == '12' and day >= '23' and day <= '31') or (month == '1' and day >= '1' and day <= '20'):
    print("Ваш знак зодиака: Козерог")
elif(month == '1' and day >= '21' and day <= '31') or ('1' <= day <= '19' and month == '2'):
    print("Ваш знак зодиака: Водолей")
elif('20' <= day <= '29' and month == '2') or ('1' <= day <= '20' and month == '3'):
    print("Ваш знак зодиака: Рыбы")
else:
    print('Проверьте данные, дата введена неправильно!')



