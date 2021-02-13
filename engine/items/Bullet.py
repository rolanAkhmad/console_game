from engine.items.item import *

class Bullet(Item):
    pass

class Bullet7_76(Bullet):
    def __init__(self):
        self.name = "Патрон 7.76 калибра"
        self.description = "Стандартный патрон 7.76 калибра"
        self.price = 8
