from buddy.src.interactive.interactive_menu import InteractiveMenu
from buddy.src.interactive.session_menu import SessionMenu
from buddy.src.interactive.list_menu import ListMenu
from buddy.src.interactive.sql_menu import SqlMenu

class MainMenu(InteractiveMenu):

    def __init__(self, manager):
        super().__init__(manager)
        self.sub_menu_modules = [
            SessionMenu(manager),
            ListMenu(manager),
            SqlMenu(manager)
        ]
