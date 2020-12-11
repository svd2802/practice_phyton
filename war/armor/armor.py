#from effects.armor_effects import ArmorEffect


class Armor:
    def __init__(self, name='default_armor', durability=100, effects=[]):
        self.name = name
        self._effects = effects
        self._durability = durability

    @property
    def durability(self):
        return self._durability

    @property
    def effects(self):
        return self._effects

    def add_effect(self, new_effect):
        if new_effect not in self.effects:
            self._effects.append(new_effect)

    def get_attack(self, damage):
        self._durability -= damage
        if self.durability <=0:
            self.durability = 0
            del self

    def __del__(self):
        del self._effects
        print("Броня " + str(self.name) + " сломана.")

    def __str__(self):
        return "Броня: " + str(self.name) + "; Прочность: " + str(self.durability) + "; Эффекты: " + str(self.effects)
