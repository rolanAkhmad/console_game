from .item import Item

class Weapon(Item):
    state = 0
    damage = 0.0
    buffs = []
    debuffs = []

class EmptyWeapon(Weapon):
    def __init__(self):
        self.name = "Отсутствует"
        self.description = ""
        self.count = 0
        self.price = 0
        self.state = 0
        self.damage = 0

class Knife(Weapon):
    pass

class Arms(Knife):
    def __init__(self):
        self.name = "Кулаки"
        self.damage = 4
        self.attack_range = 6
        self.price = 0  

class AK47(Weapon):
    def __init__(self):
        self.name = "AK47"
        self.damage = 34 
        self.attack_range = 87.73
        self.price = 768