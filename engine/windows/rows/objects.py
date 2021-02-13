class RowItem():
    title = ""
    pk = 0

    def set_primary_key(self, primary_key):
        self.pk = primary_key

class MenuRowItem(RowItem):
    def __init__(self, menu):
        pass

class TextRowItem(RowItem):
    def __init__(self, content):
        self.content = content

    def render(self):
        print(self.content)
        print()

class TextRowItemByHeader(RowItem):
    def __init__(self, header, content):
        self.header = header
        self.content = content

    def render(self):
        print(self.header)
        print(self.content)
        print()

class PlayerStatsRow(TextRowItem):
    def __init__(self, player_object):
        self.player_object = player_object

    def render(self):
        print("Статы")
        print(str(self.player_object.hp) + "/" +
                    str(self.player_object.max_hp), '|',
                    str(self.player_object.power)+'/'+
                    str(self.player_object.intelligence)+'/'+
                    str(self.player_object.endurance),'|',
                    '$', str(self.player_object.money)
        )
        print()

class PlayerWeaponsEquipRow(TextRowItemByHeader):
    def __init__(self, po):
        self.header = "Экипировка (оружие)"
        self.first, self.second, self.third = po.first_equiped_weapon, po.second_equiped_weapon, po.third_equiped_weapon

    def render(self):
        print(self.header)
        print("- осн:", self.first.name, f'({self.first.state})')
        print("- доп:", self.second.name, f'({self.second.state})')
        print("- ближ:", self.third.name, f'({self.third.state})')
        print("")

class PlayerArmorEquipRow(TextRowItemByHeader):
    def __init__(self, po):
        self.header = "Экипировка (Броня)"
        self.head_armor, self.body_armor, = po.head_armor, po.body_armor

    def render(self):
        print(self.header)
        print("- голова:", self.head_armor.name, f'({self.head_armor.state})')
        print("- туловище:", self.body_armor.name, f'({self.body_armor.state})')
        print("")

class MenuRowItem(TextRowItemByHeader):
    def __init__(self, menu):
        self.header = menu.name
        self.menu = menu

    def render(self):
        print(self.header)
        
        for menu_item in self.menu.menu_items:
            print(menu_item.keyword, menu_item.view)
        
        print("")