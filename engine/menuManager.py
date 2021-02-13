class MenuManager():
    def __init__(self):
        self.menu_list = []
        self.menu_items_list = []
        self.value = 1

    def create_menu(self, menu_name ='', menu_items=[]):
        menu = self.set_primary_keys(Menu(menu_name, menu_items))

        for menu_item in menu.menu_items:
            self.menu_items_list.append(menu_item)
        
        self.menu_list.append(menu)

        return menu

    def get_user_request(self):
        user_request = input('Введите значение: ')

        if self.keyword_is_exist(user_request):
            self.find_item_by_keyword(user_request).start_event()
        else:
            print('нет такого keyword')

    def find_item_by_keyword(self, keyword):
        for menu_item in self.menu_items_list:
            if menu_item.keyword == keyword:
                return menu_item
        return None

    def keyword_is_exist(self, keyword):
        for menu_item in self.menu_items_list:
            if menu_item.keyword == keyword:
                return True
        
        return False

    def set_primary_keys(self, menu):
        for menu_item in menu.menu_items:
            menu_item.set_primary_key(self.value)
            if menu_item.keyword == '':
                menu_item.keyword = str(menu_item.primary_key)
            
            self.value +=1
        return menu


class Menu():
    menu_items = []
    name = ''
    def __init__(self, menu_name="menu", menu_items=[]):
        self.name = menu_name
        self.menu_items = menu_items

class MenuItem():
    def __init__(self, view='пустая ячейка меню', keyword="", event = None):
        self.primary_key = 0
        self.view  = view
        self.keyword = keyword
        self.event = event

    def set_primary_key(self, pk):
        self.primary_key = pk

    def start_event(self):
        self.event()

