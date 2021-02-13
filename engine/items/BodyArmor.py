from engine.items.item import *

class Armor(Item):
    state = 0
    armor = 0
        

class EmptyArmor(Armor):
    def __init__(self):
        self.name = "Отсутствует"


class BodyArmor(Armor):
    pass

class infantryArmor(BodyArmor):
    def __init__(self):
        self.name = "Доспех гвардейца"
        self.description = "Доспех гвардейца, старый доспех давно ушедшей гвардии, очень слаб против пули"
        self.price = 87
        self.state = 100
        self.armor = 14
