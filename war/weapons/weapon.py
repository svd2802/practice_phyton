import sys
sys.path.append('C:/Users/narut/Desktop/Практикум по программированию/practice_python/war')
from exceptions import NotRealizedMethodError


class Weapon:
    def __init__(self, name='Stick', damage=1):
        self.__name = name
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def damage(self):
        raise NotRealizedMethodError()

    @damage.setter
    def damage(self, value):
        raise NotRealizedMethodError()

    def attack(self, target):
        raise NotRealizedMethodError()

    def __le__(self, other: Weapon):
        if self.damage >= other.damage:
            return self
        else:
            return other
