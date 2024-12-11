def find_closest(numbers, target):
    """
    Находит ближайшее число к целевому из списка.

    :param numbers: Список чисел.
    :param target: Целевое число.
    :return: Ближайшее число.
    """
    closest = min(numbers, key=lambda x: abs(x - target))  # Ищем минимум по разнице
    return closest



numbers = [312, 996, 31, 1991, 15]
target = 1000

result = find_closest(numbers, target)
print("Ближайшее число:", result)





























