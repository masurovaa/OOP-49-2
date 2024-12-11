
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introuduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я живу в городе {self.city}.")

    def is_adult(self):
        return self.age >= 18

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Город: {self.city}"

person1 = Person('Алтынай', 28, 'Бишкек')
person2 = Person('Ширин', 18, 'Токио')
person3 = Person('Элина', 16, 'Нью-Йорк')

person1.introuduce()
print(f"{person1.name} совершеннолетний: {person1.is_adult()}")
print(f"{person2.name} совершеннолетний: {person2.is_adult()}")
print(f"{person3.name} совершеннолетний: {person3.is_adult()}")

print(person1)
print(person2)
print(person3)






















