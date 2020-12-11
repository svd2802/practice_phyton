from __future__ import annotations
import sys
sys.path.append('C:/Users/narut/practice_python/war')
from exceptions import NotRealizedMethodError
#from effects.weapon_effects import WeaponEffect



class Weapon:
    def __init__(self, name='Stick', damage=1, effects=[]):
        self._name = name
        self._damage = damage
        self._effects = effects

    @property
    def effects(self):
        return self._effects

    @property
    def name(self):
        return self._name

    @property
    def damage(self):
        raise NotRealizedMethodError()

    @damage.setter
    def damage(self, value):
        raise NotRealizedMethodError()

    def attack(self):
        raise NotRealizedMethodError()

    def add_effect(self, new_effect):
        if new_effect not in self.effects:
            self._effects.append(new_effect)

    def __le__(self, other: Weapon):
        if self.damage <= other.damage:
            return True
        else:
            return False

    def __str__(self):
        return "Название: " + str(self.name) + "; Урон: " + str(self.damage)
