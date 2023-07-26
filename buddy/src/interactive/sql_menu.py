from interactive_menu.src.interactive_menu import InteractiveMenu
from buddy.src.io.query_runner import QueryRunner


class SqlMenu(InteractiveMenu):

    def __init__(self, manager):
        super().__init__(manager)
        self.sub_menu_modules = [
            WipeTablesMenu(manager)
        ]

    def title(self):
        return "Sql"

class WipeTablesMenu(InteractiveMenu):

    def title(self):
        return "Wipe"

    def main_loop(self):
        print("Are you sure? This is permanent!")
        answer = self.fancy_input()
        if answer in ["yes", "Yes", "ok"]:
            QueryRunner(self.manager.config).wipe_all_tables()
