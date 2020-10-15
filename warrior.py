import sys
class Warrior:
    def __init__(self, name = 'default_warrior', health = 100):
        self.name = name
        self.health  = health
        self.damage = 20
    
    def get_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            print(str(self.name) + " получил " + str(damage) + " урона. У него осталось " + str(self.health) + " здоровья.")
        else:
            return print(str(self.name) + " уже мертв.")
        if self.health <= 0:
            self.health = 0
            print(str(self.name) + " погиб.")
            
    def attack(self, target):
        if self.health == 0:
            return print(str(self.name) + " не может атаковать в таком состоянии.")            
        print(str(self.name) + " атакует война по имени " + str(target.name))
        target.get_damage(self.damage)
        if target.health == 0:
            print("Воин " + str(self.name) + " празднует победу над " + str(target.name))
            return sys.exit() 
        
    def to_string(self):
        return "Великий воин " + str(self.name) + "\nЗдоровье: " + str(self.health) + "\nУрон: " + str(self.damage)