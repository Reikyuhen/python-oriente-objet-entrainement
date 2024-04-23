from models.Character import Character
import random
from tools.Dices import Dice

class Monster(Character):

    # region construct

    def __init__(self):
        super().__init__()
        
    # endregion

    # region properties

    # endregion

    # region methodes

    def gen_inventory(self):
        gold_dice = Dice(0,5)
        leather_dice = Dice(0,3)
        list_of_item = [["Leather"],["Gold"]]
        number_of_item_leather = leather_dice.roll()
        number_of_item_gold = gold_dice.roll()
        if self.id == 1:
            wolf_loot = (number_of_item_leather*list_of_item[0])
            return wolf_loot
        elif self.id == 2:
            orc_loot = (number_of_item_gold*list_of_item[1])
            return orc_loot
        else:
            other_loot = []
            for i in range(number_of_item_leather):
                item = 0
                other_loot.append(list_of_item[item])
            for i in range(number_of_item_gold):
                item = 1
                other_loot.append(list_of_item[item])
            return other_loot

    def chara_stat(self):
        msg = "Force : " + str(self.strength) + "\n"
        msg += "Endurance : " + str(self.endurance) + "\n"
        msg += "Vie : " + str(self.health_point) + "\n"
        msg += "Inventaire : " + str(self.inventory) + "\n"
        msg += "Mort : " + str(self.dead) + "\n"
        return msg
        
    # endregion