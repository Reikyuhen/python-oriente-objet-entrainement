import random

# region constructeur

class Dice:
    def __init__(self, minimum, maximum):
        self.__minimum = minimum
        self.__maximum = maximum

    # endregion

    # region properties

    @property
    def minimum(self):
        return self.__minimum

    @property
    def maximum(self):
        return self.__maximum

    # endregion

    # region methodes

    def roll(self):
        value = random.randint(self.__minimum,self.__maximum)
        return value

    # endregion