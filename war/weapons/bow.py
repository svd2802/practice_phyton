import random

from weapon import Weapon


class Bow(Weapon):
    def __init__(self, name='Bow', damage=1, accuracy=1):
        self.__accuracy = accuracy
        super.__init__(name, damage)

    @property
    def damage(self):
        return self.accuracy * self.damage

    @damage.setter
    def damage(self, value):
        if value > 0:
            self.__damage = value
        else:
            print('Недопустимое значение урона!')

    @property
    def accuracy(self):
        return self.__accuracy

    @accuracy.setter
    def accuracy(self, value):
        if value > 0:
            self.__accuracy = value
        else:
            print('Недопустимое значение точности!')

    def attack(self):
        damage = self.accuracy * self.damage
        chance = random.randint(self.accuracy, 100)
        if chance > 60:
            return damage
        else:
            return 'Промах'
