from buddy.src.interactive.interactive_menu import InteractiveMenu

class GoalsMenu(InteractiveMenu):

    def __init__(self, manager):
        super().__init__(manager)

    def title(self):
        return "Goals"

    def main_loop(self):
        print("")
        print("------------------------------------------------------")
        print("Goals feature coming soon!")
        print("------------------------------------------------------")
        print("")
