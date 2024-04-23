from tools.Dices import Dice

def Haste_check():
    Dice_20 = Dice(1,20)
    Haste_fighter = Dice_20.roll()
    Haste_fighter += Dice_20.roll()
    Haste_fighter += Dice_20.roll()
    Haste_fighter += Dice_20.roll()
    Haste_fighter += Dice_20.roll()
    print(f"Le résultat de la hâte est de : {Haste_fighter}\n")
    return Haste_fighter
    