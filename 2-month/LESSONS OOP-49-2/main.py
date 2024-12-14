""" Наследование, полиморфизм """
""" Инкапсуляция, абстракция """

import random
#Базовый, Супер, Родительский класс
class Hero:
#атрибуты
    def __init__(self, name="John Doe", hp=100, lvl=100): #Базовое значение класса
        self.hp = hp
        self.name = name
        self.lvl = lvl
        # Защищенный атрибут
        self._luck = random.randint(0, 100)
        # Приватный атрибут
        self.__crit_dmg = random.randint(0,100)
#методы
    def __heal_hp(self):
        return random.randint(0, 100)

    def greetings(self):
        return print(f"Привет, {self.name}! \n Мой уровень: {self.lvl}.")

    def status(self):
        return  print(f"LVL: {self.lvl} \n HP: {self.hp}.")

    def attack(self):
        if self.__crit_dmg >= 30:
            return print(f'{self.name} нанес кретический удар!')
        else:
            return print(f'{self.name} нанес базовый удар.')

    def protaction(self):
        if self._luck >= 20:
            return print(f'{self.name} успешно защитился!')
        else:
            return print(f'{self.name} не смог защититься.')

    def rest(self):
        self.hp += self.__heal_hp()

hero =Hero('Боруто', 100, 1)

hero.attack()
#print(hero._luck)
#"""print(hero._Hero__crit_dmg) - не стоит использовать"""
#print(dir(hero))