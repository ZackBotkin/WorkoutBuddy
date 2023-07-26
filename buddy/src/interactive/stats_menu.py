from interactive_menu.src.interactive_menu import InteractiveMenu

class StatsMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)

    def title(self):
        return "Stats"

    def main_loop(self):
        print("")
        print("------------------------------------------------------")
        print("Stats feature coming soon!")
        print("------------------------------------------------------")
        print("")
