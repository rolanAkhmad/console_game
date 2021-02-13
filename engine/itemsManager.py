from engine.items.weapons import *

class ItemsManager():
    def give_weapon_ak47(self, person):
        ak47 = AK47()
        person.inventory__item_add(ak47)
