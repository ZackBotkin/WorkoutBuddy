from buddy.src.interactive.interactive_menu import InteractiveMenu

class StatsMenu(InteractiveMenu):

    def __init__(self, manager):
        super().__init__(manager)

    def title(self):
        return "Stats"

    def main_loop(self):
        print("")
        print("------------------------------------------------------")
        print("Stats feature coming soon!")
        print("------------------------------------------------------")
        print("")
