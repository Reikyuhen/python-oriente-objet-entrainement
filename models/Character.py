from tools.Dices import Dice
from tools.Battle import *

class Character:

    # region constructeur

    def __init__(self):
        self.__name = None
        self.__endurance = 0
        self.__strength = 0
        self.__health_point = self.__endurance
        self.__transit_hp = self.__health_point
        self.__dead = False
        self.__inventory = []

    # endregion

    # region properties

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def set_name(self, value):
        self.__name = value

    @property
    def endurance(self):
        return self.__endurance
    
    @property
    def strength(self):
        return self.__strength
    
    @property
    def health_point(self):
        return self.__health_point
    
    @property
    def transit_hp(self):
        return self.__transit_hp
    
    @transit_hp.setter
    def set_transit_hp(self, value):
        self.__transit_hp = value
    
    @property
    def dead(self):
        return self.__dead
    
    @dead.setter
    def set_dead(self, value):
        self.__dead = value
    
    @property
    def inventory(self):
        return self.__inventory
    
    @inventory.setter
    def set_inventory(self,value):
        self.__inventory = value

    # endregion
    
    # region methodes
    def Stats_creation(self):
        dice_6 = Dice(1,6)
        value_1 = dice_6.roll()
        value_2 = dice_6.roll()
        value_3 = dice_6.roll()
        value_4 = dice_6.roll()
        dice_result = []
        dice_result.append(value_1)
        dice_result.append(value_2)
        dice_result.append(value_3)
        dice_result.append(value_4)
        dice_sum = []
        while len(dice_sum) != 3 :
            for i in range(len(dice_result)):
                maximum_value = max(dice_result)
            dice_sum.append(maximum_value)
            dice_result.remove(maximum_value)
        dice_sum = sum(dice_sum)
        return dice_sum
    
    def Check_endurance(self,endurance_value):
        health_bonus = 0
        if endurance_value < 5:
            health_bonus -= 1
        elif endurance_value < 10:
            health_bonus += 0
        elif endurance_value < 15:
            health_bonus += 1
        else:
            health_bonus += 2
        endurance_value += health_bonus
        return endurance_value

    def Hit(self):
        dice_4 = Dice(1,4)
        damage = dice_4.roll()
        bonus_damage = 0
        msg = "Le dé de dégat équivaut à " + str(damage)
        if self.strength < 5:
            bonus_damage -= 1
        elif self.strength < 10:
            bonus_damage += 0
        elif self.strength < 15:
            bonus_damage += 1
        else:
            bonus_damage += 2
        msg += " avec un bonus de " + str(bonus_damage) + "."
        print(msg)
        damage += bonus_damage
        return damage
    
    def Take_damage(self, damage):
        hit_end = self.transit_hp - damage
        self.set_transit_hp = hit_end
        print(f"{self.name} a subi {damage} de dégats.")
        
    def Rest(self):
        self.set_transit_hp = self.health_point
    
    def Fight(self, opponent):
        Haste_Attacker = Haste_check()
        Haste_Defender = Haste_check()
        engage = True
        while engage:
            if Haste_Attacker > Haste_Defender :
                while self.transit_hp > 0 and opponent.transit_hp > 0 :
                    print(f"{self.name} attaque ...")
                    opponent.Take_damage(self.Hit())
                    print(f"{opponent.name} point de vie : {opponent.transit_hp}\n")
                    if opponent.transit_hp > 0 :
                        print(f"{opponent.name} riposte ...")
                        self.Take_damage(opponent.Hit())
                        print(f"{self.name} point de vie : {self.transit_hp}\n")
                        if self.transit_hp <= 0 :
                            engage = False
                    else:
                        engage = False
            elif Haste_Defender > Haste_Attacker :
                while self.transit_hp > 0 and opponent.transit_hp > 0 :
                    print(f"{opponent.name} attaque ...")
                    self.Take_damage(opponent.Hit())
                    print(f"{self.name} point de vie : {self.transit_hp}\n")
                    if self.transit_hp > 0 :
                        print(f"{self.name} riposte ...")
                        opponent.Take_damage(self.Hit())
                        print(f"{opponent.name} point de vie : {opponent.transit_hp}\n")
                        if opponent.transit_hp <= 0 :
                            engage = False
                    else:
                        engage = False
            else:
                Haste_Attacker = Haste_check()
                Haste_Defender = Haste_check()
                
    # endregion