from interactive_menu.src.interactive_menu import InteractiveMenu

class GoalsMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)

    def title(self):
        return "Goals"

    def main_loop(self):
        print("")
        print("------------------------------------------------------")
        print("Goals feature coming soon!")
        print("------------------------------------------------------")
        print("")
