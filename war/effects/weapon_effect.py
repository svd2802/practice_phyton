from __future__ import annotations

# from warrior import Warrior

from effects.effect import Effect


class WeaponEffect(Effect):
    def __init__(self, name, power=10, round=2):
        Effect.__init__(self, name=name, power=power)
        self.__round = round

    def fire(self, target: Warrior):
        damage = round(0.05 * target.health, 4)
        target.health = target.health - damage
        print(f'Огонь наносит {target.name} {damage} урона.')

    @property
    def round(self):
        return self.__round

    @round.setter
    def round(self, value):
        if value > 0 and value <= 10:
            self.__round = value

    def __str__(self):
        return Effect.__str__(self) + ", действует {} раундов".format(self.__round)
