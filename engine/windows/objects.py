from .rows.wrmanager import WindowRowsManager
from .rows.objects import *
from engine.menuManager import MenuManager

import os

# Предствление окна
class Window():
    def __init__(self):
        self.is_active = True
        self.pk = 0
        self.rows_manager = WindowRowsManager()
        self.menu_manager = MenuManager()
    
    def render(self):
        while self.is_active:
            self.clear_window_data()
            self.rows_manager.render_rows()
            self.menu_manager.get_user_request()
        
    def set_primary_key(self, pk):
        self.pk = pk
    
    def clear_window_data(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def close(self):
        self.clear_window_data()
        self.is_active = False

