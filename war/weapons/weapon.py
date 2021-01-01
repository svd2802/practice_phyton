from __future__ import annotations

from effects.weapon_effect import WeaponEffect
from exceptions import NotRealizedMethodError


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

    def __lt__(self, other: Weapon):
        if self.damage < other.damage:
            return True
        else:
            return False

    def __str__(self):
        if self.effects is not None and len(self.effects) > 0:
            effects_str = ' '
            for i in self.effects:
                if i is not None:
                    effects_str += i.name + "; "
            return "Название: " + str(self.name) + "; Урон: " + str(round(self.damage, 2)) + "; Эффекты: " + effects_str
        else:
            return "Название: " + str(self.name) + "; Урон: " + str(round(self.damage, 2))
