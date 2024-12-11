# 1. Функция для нахождения ближайшего числа и сортировки списка
def nearest_number(numbers, target):
    sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))
    return target, tuple(sorted_numbers)

numbers = [10, 3, 7, 20, 15]
target = 12
result = nearest_number(numbers, target)
print(result)  # (12, (10, 15, 7, 20, 3))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8]

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # [2, 4, 6, 8, 10]

def get_element(iterable=[1, 2, 3, 4, 5]):
    while True:
        try:
            index = int(input(f"Введите индекс от 0 до {len(iterable) - 1} (или -1 для выхода): "))
            if index == -1:
                print("Выход из программы.")
                break
            print(f"Элемент на индексе {index}: {iterable[index]}")
        except ValueError:
            print("Ошибка: индекс должен быть числом.")
        except IndexError:
            print(f"Ошибка: введите индекс в диапазоне от 0 до {len(iterable) - 1}.")

get_element(["a", "b", "c", "d"])


















