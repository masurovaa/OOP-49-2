""" HW2 - Наследование, полиморфизм. """

#Базовый, Супер, Родительский класс
class Hero:
#атрибуты
    def __init__(self, name="John Doe", hp=100): #Базовое значение класса
        self.hp = hp
        self.name = name
#методы
    def rest(self):
        self.hp += 10
        return f"{self.name} востанавливает здоровье на +10, текущее HP: {self.hp}."

    def action(self):
        return f"{self.name} делает базовое действие."

hero = Hero('Kirito', 100)

#print(hero.rest())
#print(hero.action())


""" Наследование """
# Дочерний класс
class Warrior(Hero):
    #pass - если оставить пустым, все унаследует у родительского класса.
#можно добавить свои атрибуты дочернего класса
    def __init__(self, name, hp, st):
        super().__init__(name, hp) #наследовали все атрибуты родительского класса
        self.st = st


# можно добавить свои методы дочернего класса
    def attack(self):
        if self.st >= 10:
            self.st -= 10
            return f'{self.name} превращается в алмаза.'
        else:
            return f'{self.name} стамина меньше 10.'

hero_warrior = Warrior('Ben-10', 1000, 100)


#print(hero_warrior.rest())
#print(hero_warrior.action())
#print(hero_warrior.attack())

""" Полиморфизм """ # Изменили метод в дочернем классе не изменяя метод в родительском классе.
class Mage(Hero):

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self.mp = mp

    def rest(self):
        self.mp += 100
        return f'{self.name} восстанавливает ману на 100, текущий MP: {self.mp}'

    def attack(self):
        if self.mp >= 10:
            self.mp -= 10
            return f'{self.name} калдует огненным шаром'
        else:
            return f'{self.name} мана меньше 10'

# Перед изменением метода уноследовали родительский метод и обратились внутреннему методу. Полиморфизм с наследованием*.
    def action(self):
        old_action = super().action()
        attack = self.attack()
        return f'{old_action} {attack}'


hero_mage = Mage('Magnus', 100, 1000)

#print(hero_mage.rest())
#print(hero_mage.action())
#print(hero_mage.attack())


""" Добавляем новый класс-наследник. """
class Archer(Hero):

# наследуем атрибуты родительского класса и добавляем новые атрибуты лучника
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows >= 10 and self.precision >= 1:
            self.arrows -= 1
            return f'{self.name} удачно атаковал!'
        elif self.precision == 0:
            return f'{self.name} неудачно атаковал!'
        else:
            return f'{self.name} не смог атаковать!!!'

    def rest(self):
        self.arrows += 5
        return f'{self.name} пополняет количество стрел на 5, arrows: {self.arrows}'

    def actions(self):
        hero_actions = super().action()
        return f'{hero_actions} {self.rest()}'

hero_archer = Archer('Артур', 100, 20, 10)

print(hero_archer.rest())
print(hero_archer.attack())
#print(hero_archer.action())
#print(hero_archer.actions())











