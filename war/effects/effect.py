from exceptions import NotRealizedMethodError


class Effect:
    def __init__(self, name=None, power=10):
        self.__name = name
        self.__power = power

    @property
    def name(self):
        return self.__name

    @property
    def power(self):
        return self.__power

    @name.setter
    def name(self, value):
        self.__name = value

    @power.setter
    def power(self, value):
        if value > 0:
            self.__power = round(float(value), 2)

    def __str__(self):
        return '{}, уровень: {}'.format(self.name, self.power)
