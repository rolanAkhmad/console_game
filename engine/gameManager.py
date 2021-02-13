from engine.windowsManager import WindowsManager
from engine.items.Person import Person
from engine.windows.objects import Window
from engine.menuManager import *
from engine.windows.rows.objects import *
from functools import partial       

class GameManager():
    def __init__(self):
        self.windows_manager = WindowsManager()
        self.player = Person()
        self.main_menu()

    def quit_game(self):
        self.windows_manager.delete_all_windows()

    def main_menu(self):
        window = Window()

        main_menu = window.menu_manager.create_menu(
            menu_name="Главное меню",
            menu_items=[
                MenuItem(view='Начать игру', event = partial(self.player_window, self.player)),
                MenuItem(view='Выход', event = self.quit_game),
            ]
        )

        window.rows_manager.add_rows([
            MenuRowItem(main_menu)
        ])

        self.windows_manager.create_window(window)

    # def inventory_window(self, player_object:Person):
    #     inventory_window = Window()
        
    #     player_object.inventory.

    #     inventory_menu = inventory_window.menu_manager.create_menu(
    #         menu_name = 'Меню инвентаря',
    #         menu_items = 
    #     )

    def player_window(self, player_object:Person):
        window = Window()

        player_menu = window.menu_manager.create_menu(
            menu_name='player_menu',
            menu_items=[
                MenuItem(view='Инвентарь', ),
            ]
        )

        window_menu = window.menu_manager.create_menu(
            menu_name='window_menu',
            menu_items=[
                MenuItem(keyword='q', view='Назад/Выход', event=self.windows_manager.close_and_get_prev)
            ]
        )

        window.rows_manager.add_rows([
            TextRowItem(player_object.name),
            TextRowItemByHeader("Описание:", player_object.description),
            PlayerStatsRow(player_object),
            PlayerWeaponsEquipRow(player_object),
            PlayerArmorEquipRow(player_object),
            MenuRowItem(player_menu),
            MenuRowItem(window_menu)
        ])

        self.windows_manager.create_window(window)
