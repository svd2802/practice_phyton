from warrior import Warrior
import random

a = Warrior('Abe')
b = Warrior('Bjorn')
c = Warrior('Sigmair')
temp = [a,b,c]
while True:
    if len(temp) > 1:
        duel = random.sample(temp, 2)
        if duel[1].health > 0:
            duel[0].attack(duel[1])
            print()
        else:
            break
    else:
        print("Недостаточно участников.")
        break