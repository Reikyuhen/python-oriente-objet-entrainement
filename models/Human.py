from models.Hero import Hero

class Human(Hero):

    # region constructeur

    def __init__(self):
        super().__init__()
        self.__name = input("Quel est votre nom courageux humain ?")
        self.__strength = self.Stats_creation() + 1
        self.__endurance = self.Stats_creation() + 1
        self.__health_point = self.Check_endurance(self.__endurance)
        self.__transit_hp = self.__health_point
        self.__inventory = []

    # endregion

    # region properties

    @property
    def name(self):
        return self.__name
    
    @property
    def strength(self):
        return self.__strength
    
    @property
    def endurance(self):
        return self.__endurance
    
    @property
    def health_point(self):
        return self.__health_point
    
    @property
    def get_transit_hp(self):
        return self.__transit_hp
    
    @get_transit_hp.setter
    def set_transit_hp(self,value):
        self.__transit_hp = value
    
    @property
    def inventory(self):
        return self.__inventory
    
    @inventory.setter
    def set_inventory(self,value):
        self.__inventory = value
    
    # endregion

    # region methodes

    def chara_stat(self):
        id = "Héros : " + self.__name + " l'humain.\n" 
        msg = super().chara_stat()
        return print(id + msg)
    
    # endregion