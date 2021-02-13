from engine.items.BodyArmor import *
from engine.invetoryManager import InventoryManager
from engine.items.weapons import *
from engine.items.Bullet import *

class Person():
    def __init__(self):
        self.inventory = InventoryManager()
        self.description = "player description"
        self.name = "person_object"
        self.money = 0
        self.hp = 100
        self.max_hp = 100
        
        self.first_equiped_weapon = AK47()
        self.second_equiped_weapon = EmptyWeapon()
        self.third_equiped_weapon = EmptyWeapon()

        self.head_armor = EmptyArmor()
        self.body_armor = EmptyArmor()

        self.intelligence = 0
        self.power = 0
        self.endurance = 0