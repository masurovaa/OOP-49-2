""" Инкапсуляция - Абстракция """
from abc import ABC, abstractmethod
import random

class Hero(ABC):

    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        #защищенный атрибут
        self._luck = random.randint(0, 100)
        #приватный атрибут
        self.__crit_dmg = random.randint(0, 100)

    def __heal_hp(self):
        return random.randint(0, 100)

    def greetings(self):
        return print(f'Привет, {self.name}! \n Мой уровень {self.lvl}')

    def status(self):
        return print(f'LVL: {self.lvl}! \n HP: {self.hp}')

    def attack(self):
        if self.__crit_dmg >= 30:
            return print(f'{self.name} базовый удар!')

    def protection(self):
        if self._luck >= 20:
            return print(f'{self.name} успешно защищается!')
        else:
            return print(f'{self.name} не смог защититься!')


    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass


#hero = Hero('Боруто', 100, 1)
#hero.protection()
#hero.attack()

class ShieldHero(Hero):

    def __init__(self, name, hp, lvl, aura=0):
        super().__init__(name, hp, lvl)
        self.aura = aura


    def protection(self):
        if self._luck >= 20:
            return print(f'{self.name} выполняет уникальную атаку!')
        else:
            return print(f'{self.name} не смог выполнить уникальную атаку!')

    def unique_attack(self):
       if self.aura >= 10:
           return print(f'')







""" Множественное наследование """
#
#












