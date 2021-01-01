from effects.effect import Effect


class ArmorEffect(Effect):
    def __init__(self, name=None, power=10):
        Effect.__init__(self, name=name)
        self.__power = power

    @property
    def round(self):
        return self.__round

    @round.setter
    def round(self, value):
        if value > 0 and value <= 10:
            self.__round = value
