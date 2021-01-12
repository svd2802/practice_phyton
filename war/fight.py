import random

from armor.armor import Armor
from effects.weapon_effect import WeaponEffect
from effects.armor_effect import ArmorEffect
from warrior import Warrior
from weapons.bow import Bow
from weapons.sword import Sword
from weapons.weapon import Weapon


def main():
    armor_effect = [ArmorEffect('frost'), ArmorEffect('fire')]
    weapon_effect = [WeaponEffect('frost', 20, 2), WeaponEffect('fire', 1, 2)]
    temp = [Warrior('Abe', health=300, weapons=[Sword(name='Frost Sword', effects=weapon_effect[0]), Sword()]), Warrior('Bjorn', health=300, weapons=[
        Sword()], armor=Armor(effects=armor_effect)), Warrior('Sigmair', health=300, weapons=[Sword(), Bow(effects=weapon_effect[1])])]

    while True:
        if len(temp) > 1:
            duel = random.sample(temp, 2)
            if duel[1].health > 0 and duel[0].health > 0:
                duel[0].attack(duel[1])
                print()
                if duel[1].health == 0:
                    temp.remove(duel[1])
        elif len(temp) == 1:
            break
        else:
            print("Недостаточно участников.")
            break


if __name__ == "__main__":
    main()
