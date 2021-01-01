from __future__ import annotations

import copy

from armor.armor import Armor
from effects.weapon_effect import WeaponEffect
from weapons.weapon import Weapon


class Warrior:

    def __init__(self, name='default_warrior', health=100, damage=20, armor=None, weapons=[]):
        self._name = name
        self._health = health
        self._damage = damage
        self._armor = armor
        self._weapons = weapons
        self._effects = {'normal': 0}

    def attack(self, target):
        target.next_round()
        if self._effects.get('frost') is not None and self._effects.get('frost') > 0:
            self.next_round()
            return print(str(self.name) + " заморожен и не может атаковать в таком состоянии.")
        self.next_round()
        if len(self.weapons) != 0:
            self.weapons.sort(reverse=True)
        if len(self.weapons) == 0:
            print(str(self.name) + " атакует война " +
                  str(target.name) + " кулаками.")
            target.get_attack(self.damage, self.weapons[0].effects)
        else:
            print(str(self.name) + " атакует война " +
                  str(target.name) + " с помощью " + (self.weapons[0].name))
            weapon_damage = self.weapons[0].attack()
            if weapon_damage != 'Промах':
                target.get_attack(weapon_damage, self.weapons[0].effects)
            else:
                print(str(self.name) + " промахивается.")
        if target.health == 0:
            print(str(self) + " празднует победу над " + str(target.name))
            self.get_weapons(target.weapons)
            del target

    def get_weapons(self, weapons):
        other_weapons = copy.deepcopy(weapons)
        self.weapons.extend(other_weapons)

    def get_attack(self, damage, effects):
        if self.armor is not None and self.armor.durability > 0:
            gotten_effects = self.armor.get_gotten_effects(effects)
            self.armor.get_attack(damage, effects)
            if len(gotten_effects) > 0:
                for i in gotten_effects:
                    self.effects.update({i: i.round})
        else:
            self.get_damage_without_armor(damage)
            debuff_duration = []
            print(self.effects)
            for i in effects:
                if i is not None:
                    self.effects.update({i: i.round})
                    debuff_duration.append(i.round)
            if len(debuff_duration) > 0:
                debuff_duration.sort()
                self.effects.update({'normal': debuff_duration[-1]})

    def get_damage_without_armor(self, damage):
        if self.health > 0:
            self.health -= damage
            print(str(self.name) + " получил " + str(damage) +
                  " урона. У него осталось " + str(self.health) + " здоровья.")
        if self.health <= 0:
            self.health = 0
            print(str(self.name) + " погиб.")

    def next_round(self):
        # уменьшаем длительность эффектов на 1 ход
        if self.effects['normal'] != 0:
            for i in self.effects.items():
                if i[1] > 0:
                    self.effects.update({i[0]: i[1] - 1})
                    if i[0] != 'normal' and i[0].name == 'fire':
                        i[0].fire(self)

    @property
    def effects(self):
        return self._effects

    @property
    def health(self):
        return self._health

    @property
    def armor(self):
        return self._armor

    @property
    def weapons(self):
        return self._weapons

    @property
    def name(self):
        return self._name

    @property
    def damage(self):
        return self._damage

    @health.setter
    def health(self, value):
        self._health = round(value, 2)

    @armor.setter
    def armor(self, armor: Armor):
        self._armor = armor

    def __del__(self):
        print("Valhalla, " + str(self.name) + " is coming.")

    def __str__(self):
        weapons_str = ""
        for i in self.weapons:
            weapons_str += str(i) + "; "
        effects_str = " "
        for item in self.effects.items():
            if item[0] != 'normal':
                effects_str += item[0].name + " " + str(item[1]) + " ходов, "
        return "Великий воин " + str(self.name) + effects_str + "Здоровье: " + str(self.health) + "; Урон: " + str(self.damage) + "; Оружие: " + weapons_str
