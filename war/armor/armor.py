from effects.armor_effect import ArmorEffect


class Armor:
    def __init__(self, name='default_armor', durability=100, effects=[]):
        self.name = name
        self._effects = list(effects)
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

    def get_attack(self, damage, effects):
        self._durability -= damage
        print(f"Броня поглотила {damage} урона.")
        # self.get_gotten_effects(effects)
        if self.durability <= 0:
            self._durability = 0
            del self

    def get_gotten_effects(self, effects):
        # проверяем резисты и формируем list лист полученных дебаффов
        # print("get_gotten_effects")
        result_effects = []
        if effects is not None and self.effects is not None:
            for i in effects:
                if i is not None:
                    result_effects.append(self.check_resistance_to_effect(i))
        return result_effects

    def check_resistance_to_effect(self, effect):
        for i in self.effects:
            if i == effect and i.power >= effect.power:
                print(f'Броня {self.name} поглащает эффект {effect.name}')
                continue
            else:
                return effect

    def __del__(self):
        del self._effects
        print("Броня " + str(self.name) + " сломана.")

    def __str__(self):
        if len(self.effects) > 0:
            effects_str = ''
            for i in self.effects:
                effects_str += i.name + "; "
            return "Броня: " + str(self.name) + "; Прочность: " + str(self.durability) + "; Эффекты: " + effects_str
        else:
            return "Броня: " + str(self.name) + "; Прочность: " + str(self.durability)
