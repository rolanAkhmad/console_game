from engine.windows.objects import *

class WindowRowsManager():
    def __init__(self):
        self.rows = []

    def add_rows(self, row_items):
        for row_item in row_items:
            self.rows.append(row_item)

    def render_rows(self):
        for row in self.rows:
            row.render()