from interactive_menu.src.interactive_menu import InteractiveMenu

class ListMenu(InteractiveMenu):

    def __init__(self, manager):
        super().__init__(manager)

    def title(self):
        return "List"

    def main_loop(self):
        self.manager.print_todays_workouts()
