from models.Human import Human
from models.Dwarf import Dwarf
from models.Wolf import Wolf
from models.Orc import Orc
from models.Dragon_Whelp import Dragon_Whelp
wolf1 = Wolf()
wolf1.chara_stat()
orc1 = Orc()
orc1.chara_stat()
dragon_Whelp1 = Dragon_Whelp()
dragon_Whelp1.chara_stat()

human1 = Human()
human1.chara_stat()
dwarf1 = Dwarf()
dwarf1.chara_stat()

human1.Fight(wolf1)

dwarf1.Fight(orc1)

wolf1.chara_stat()
orc1.chara_stat()
human1.chara_stat()
dwarf1.chara_stat()