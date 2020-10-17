import random

from weapon import Weapon


class Sword(Weapon):
    def __init__(self, name='Sword', damage=1):
        self.__durability = 1
        super().__init__(name, damage)

    @property
    def damage(self):
        return self.durability * self.damage

    @damage.setter
    def damage(self, value):
        if value > 0:
            self.__damage = value
        else:
            print('Недопустимое значение урона!')

    @property
    def durability(self):
        return self.__durability

    def wearout(self):
        self.__durability *= 0.9

    def attack(self):
        damage = self.damage * self.durability
        wearout_chance = random.randint(0, 1)
        if wearout_chance == 1:
            self.wearout()
        return damage
