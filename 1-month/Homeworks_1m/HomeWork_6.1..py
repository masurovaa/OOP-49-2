#Функция “Ближайшее Число”.
def nearest_number(numbers, target=0):
    return min(numbers, key=lambda x: abs(x - target))

while True:
    try:
        numbers = [float(num.strip()) for num in input("Введите числа через пробел:").split()]
        break
    except ValueError:
        print("Ошибка: Введите только числа.")
while True:
    try:
        target = float(input("Введите целое число:"))
        break
    except ValueError:
         print("Ошибка: Введите корректное число.")
result = nearest_number (numbers, target)
print(f"Ближайшее число к {target}: {result}")
