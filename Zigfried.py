import random

def hp_Zig():
    hp_Zigfried = int(input("Enter HP of Zigfried The Greatest: "))
    return hp_Zigfried

def damage_Zig():
    damage_Zigfried = int(input("Enter damage of Zigfried The Greatest: "))
    return damage_Zigfried

def armor_Zig():
    armor_Zigfried = int(input("Enter armor of Zigfried The Greatest: "))
    return armor_Zigfried

def stats_Zig(hp, damage, armor):
    print("\nZigfried's HP :{} \nZigfried's damage: {} \nZigfried's armor: {}".format(hp, damage, armor))

def zig_attack(hp, attack, armor):
    if random.randint(1,10) % 2 != 0:
        hp -= (attack - armor)
        print("\nZigfried attacked lord on {} \nLord has {} HP".format(attack - armor, hp))
    else:
        hp -= attack 
        print("\nZigfried critical attacked lord on {} \nLord has {} HP".format(attack, hp))
    return hp