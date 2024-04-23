from models.Monster import Monster
import random

class Wolf(Monster):

    # region constructeur

    def __init__(self):
        super().__init__()
        self.__name = "loup"
        self.__id = 1
        self.__strength = self.Stats_creation()
        self.__endurance = self.Stats_creation()
        self.__health_point = self.Check_endurance(self.__endurance)
        self.__transit_hp = self.__health_point
        self.__inventory = self.gen_inventory()

    # endregion

    # region properties

    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
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
        list_of_grade = ["Grand ","Petit ","Chef ","Alpha "]
        randomizer_grade = random.randint(0,len(list_of_grade)-1)
        grade = list_of_grade[randomizer_grade]
        list_of_color = [" gris"," brun"," noir"," blanc"]
        randomizer_color = random.randint(0,len(list_of_color)-1)
        color = list_of_color[randomizer_color]
        pseudo = "Monstre : " + grade + self.__name + color + ".\n" 
        msg = super().chara_stat()
        return print(pseudo + msg)
    
    # endregion