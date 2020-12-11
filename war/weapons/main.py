#from weapon import Weapon
from sword import Sword
from bow import Bow

def main():
    #stick = Weapon()
    # throws new excetion
    #print(stick.name, stick.damage)
    #stick.attack(None)
    common_sword = Sword()
    #print(common_sword.pro)
    common_bow = Bow()
    common_bow.damage = 4
    common_bow.accuracy = 5
    highest_damage_weapon = common_sword <= common_bow
    print(highest_damage_weapon, common_sword, common_bow)


if __name__ == "__main__":
    main()
