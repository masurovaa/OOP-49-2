""" ООП - Объектно-ориентированное программирование. """
# ООП - (Объектно-ориентированное программирование) - это парадигма программирования, основанная на концепции объектов,
# которые объединяют данные (атрибуты) и логику (методы).

# ООП - Обьекторно-ориентированное программирование
# Наследование
# Полиморфизм
# Инкапсуляция
# Абстракция


class Car:

    def __init__(self, this_model, this_year, this_color):
        # Атрибуты класса/Field
        self.model = this_model
        self.year = this_year
        self.color = this_color

    # Методы класса
    def signal(self):
        print(f"{self.model} signal!")

    def max_speed(self):
        if self.model == "BMW":
            print("Супер быстрая машина")
        else:
            print('просто быстрая')

    def __str__(self):
        return f'Model: {self.model}, Color: {self.color}, Year: {self.year}'


# Экземпляр класса
car_bmw = Car("BMW", 2004, 'silver')
car_honda = Car("Fit", 2004, 'Red')



print(car_honda)
print(car_honda.model)





























