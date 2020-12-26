import random

from weapons.weapon import Weapon
print(dir())


class Sword(Weapon):
    def __init__(self, name='Sword', damage=10):
        Weapon.__init__(self, name, damage)
        self._durability = 1
        
    @property
    def damage(self):
        return self.durability * int(self._damage)

    @damage.setter
    def damage(self, value):
        if value > 0:
            self._damage = value
        else:
            print('Недопустимое значение урона!')

    @property
    def durability(self):
        return self._durability

    def wearout(self):
        self._durability *= 0.9

    def attack(self):
        damage = round(self._damage * self._durability)
        wearout_chance = random.randint(0, 1)
        if wearout_chance == 1:
            self.wearout()
        return damage
