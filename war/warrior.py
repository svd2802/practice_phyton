class Warrior:
    def __init__(self, name='default_warrior', health=100, damage=20):
        self.name = name
        self.health = health
        self.damage = damage

    def get_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            print(str(self.name) + " получил " + str(damage) +
                  " урона. У него осталось " + str(self.health) + " здоровья.")
        if self.health <= 0:
            self.health = 0
            print(str(self.name) + " погиб.")

    def attack(self, target):
        if self.health == 0:
            return print(str(self.name) + " не может атаковать в таком состоянии.")
        print(str(self.name) + " атакует война по имени " + str(target.name))
        target.get_damage(self.damage)
        if target.health == 0:
            print(self.to_string() + "; празднует победу над " + str(target.name))
            del target

    def __del__(self):
        print("Valhalla, " + str(self.name) + " is coming.")

    def to_string(self):
        return str("Великий воин " + str(self.name) + "; Здоровье: " + str(self.health) + "; Урон: " + str(self.damage))
