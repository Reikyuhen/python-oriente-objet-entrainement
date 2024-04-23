from models.Character import Character

class Hero(Character):

    # region construct

    def __init__(self):
        super().__init__()
        
    # endregion

    # region properties

    # endregion

    # region methodes

    def chara_stat(self):
        msg = "Force : " + str(self.strength) + "\n"
        msg += "Endurance : " + str(self.endurance) + "\n"
        msg += "Vie : " + str(self.health_point) + "\n"
        msg += "Inventaire : " + str(self.inventory) + "\n"
        msg += "Mort : " + str(self.dead) + "\n"
        return msg
    
    def health_state(self):
        msg = "Point de vie actuel : " + str(self.transit_hp) + "\n"
        return print(msg)
    
    def cut_up(self,opponent):
        opp_inventory = opponent.inventory
        group_of_elem = 0
        while group_of_elem < len(opp_inventory):
            for element in range (len(opp_inventory[group_of_elem])):
                self.set_inventory.append(opp_inventory[group_of_elem])
                if opp_inventory[group_of_elem][element] == "Leather":
                    print("Vous avez trouvé du cuir.")
                elif opp_inventory[group_of_elem][element] == "Gold":
                    print("Vous avez trouvé de l'or")
            group_of_elem += 1
        opponent.set_inventory = []
    
    def Fight(self, opponent):
        super().Fight(opponent)
        if self.get_transit_hp <= 0:
            print(f"{self.name} est mort... *musique triste*\n")
            self.set_dead = True
            self.set_inventory = []
        else:
            print("Victoire ! *applaudissement*\n")
            opponent.set_dead = True
            self.cut_up(opponent)
            self.Rest()
        
    # endregion