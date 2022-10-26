import random

def hp_lord():
    hp_Lord = int(input("Enter HP of Lordfried The Greatest: "))
    return hp_Lord

def damage_lord():
    damage_Lord = int(input("Enter damage of Lord The Greatest: "))
    return damage_Lord

def armor_lord():
    armor_Lord = int(input("Enter armor of Lord The Greatest: "))
    return armor_Lord

def stats_lord(hp, damage, armor):
    print("\nLord's HP :{} \nLord's damage: {} \nLord's armor: {}".format(hp,damage, armor))

def lord_attack(hp, attack, armor):
    if random.randint(1,10) % 2 != 0:
        hp -= (attack - armor)
        print("\nLord attacked zigfried on {} \nZigfried has {} HP".format(attack - armor, hp))
    else:
        print("\nLord missed attack on Zigfried \nZigfried has {} HP".format(hp))
    return hp