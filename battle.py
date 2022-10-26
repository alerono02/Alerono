from Zigfried import *
from Lord import *
import random

hp1 = hp_Zig()
damage1 = damage_Zig()
armor1 = armor_Zig()

hp2 = hp_lord()
damage2 = damage_lord()
armor2 = armor_lord()

stats_Zig(hp1, damage1, armor1)
stats_lord(hp2, damage2, armor2)

while hp1 > 0 and hp2 > 0:
    hp2 = zig_attack(hp2,damage1,armor2)
    if hp2 > 0:
        hp1 = lord_attack(hp1,damage2,armor1)
    else:
        break

if hp1 <= 0:
    print("\nZigdried the Greatest lose. Lord of the Forest is a winer! ")
else:
    print("\nLord of the Forest lose. Zigfried the Greatest is a winer")
