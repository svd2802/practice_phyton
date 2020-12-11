from armor.armor import Armor
from weapons.weapon import Weapon
import copy


class Warrior:
    def __init__(self, name='default_warrior', health=100, damage=20, armor=None, weapons=[]):
        self.name = name
        self.health = health
        self.damage = damage
        self._armor = armor
        self._weapons = weapons

    def get_damage_without_armor(self, damage):
        if self.health > 0:
            self.health -= damage
            print(str(self.name) + " получил " + str(damage) +
                  " урона. У него осталось " + str(self.health) + " здоровья.")
        if self.health <= 0:
            self.health = 0
            print(str(self.name) + " погиб.")

    def attack(self, target):
        self.weapons.sort()
        if self.health == 0:
            return print(str(self.name) + " не может атаковать в таком состоянии.")
        print(str(self.name) + " атакует война по имени " + str(target.name))
        if len(self.weapons) == 0:
            target.get_attack(self.damage)
        else:
            weapon_damage = self.weapons[0].attack()
            if weapon_damage != 'Промах':
                target.get_attack(weapon_damage)
        if target.health == 0:
            print(str(self) + "; празднует победу над " + str(target.name))
            self.get_weapons(target.weapons)
            del target

    @property
    def armor(self):
        return self._armor

    @property
    def weapons(self):
        return self._weapons

    def get_weapons(self, weapons):
        other_weapons = copy.deepcopy(weapons)
        self.weapons.append(other_weapons)
        
    def get_attack(self, damage):
        if self.armor.durability != 0:
            self.armor.get_attack(damage)
        else:
            self.get_damage_without_armor(damage)

    def __del__(self):
        print("Valhalla, " + str(self.name) + " is coming.")

    def __str__(self):
        return "Великий воин " + str(self.name) + "; Здоровье: " + str(self.health) + "; Урон: " + str(self.damage) + "; Оружие: " + str(self.weapons)
