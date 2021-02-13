from engine.menuManager import *

class WindowsManager():
    def __init__(self):
        self.windows = []                   # содержит все открытые окна
        self.current_window = None          # содержит текущее открытое окно

    def render_current_window(self):
        
        self.current_window.render()

    def create_window(self, window):
        self.append_window_and_set_pk(window)
        self.current_window.render()
            
    def delete_all_windows(self):
        self.current_window.close()

        for window in self.windows:
            window.close()

    def append_window_and_set_pk(self, window):
        window.set_primary_key(self.windows.count)  
        self.windows.append(window)
        self.current_window = window

    def get_window_by_pk(self, pk):
        for window in self.windows:
            if pk == window.pk:
                return window
        
    def close_and_get_prev(self):
        self.current_window = self.windows[-2]
        self.windows.pop()
        self.current_window.render()

