import random

from weapons.weapon import Weapon


class Bow(Weapon):
    def __init__(self, name='Bow', damage=2, accuracy=10):
        Weapon.__init__(self, name, damage)
        self.__accuracy = accuracy

    @property
    def damage(self):
        return self.__accuracy * int(self._damage)

    @damage.setter
    def damage(self, value):
        if value > 0:
            self._damage = value
        else:
            print('Недопустимое значение урона!')

    @property
    def accuracy(self):
        return self.__accuracy

    @accuracy.setter
    def accuracy(self, value):
        if value > 0 and value <= 100:
            self.__accuracy = value
        elif value > 100:
            self.__accuracy = 100
        else:
            print('Недопустимое значение точности!')

    def attack(self):
        damage = self.damage
        chance = random.randint(self.accuracy, 100)
        if chance > 60:
            return damage
        else:
            return 'Промах'
