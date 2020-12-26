import random

from warrior import Warrior
from armor.armor import Armor
from weapons.weapon import Weapon
from weapons.sword import Sword
from weapons.bow import Bow


def main():
    # stick = Weapon()
    # common_sword = Sword()
    temp = [Warrior('Abe', weapons=[Sword(), Sword()]), Warrior('Bjorn', weapons=[
        Bow(), Sword()]), Warrior('Sigmair', weapons=[Sword(), Bow()])]

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
