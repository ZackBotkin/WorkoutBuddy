from interactive_menu.src.interactive_menu import InteractiveMenu


class SessionMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)
        self.sub_menu_modules = [
            PullupMenu(manager, self.path),
            PushupMenu(manager, self.path),
            BicepMenu(manager, self.path),
            PlankMenu(manager, self.path),
            ShoulderMenu(manager, self.path),
            LatsMenu(manager, self.path),
            BikesMenu(manager, self.path)
        ]

    ## TODO : rename this whole thing "Record" session is kind of dumb
    def title(self):
        return "Record"

class PullupMenu(InteractiveMenu):
    def title(self):
        return "Pullups"
    def main_loop(self):
        print("Count?")
        count = self.fancy_input()
        if count.isdigit():
            self.manager.insert_pullups(count)
        else:
            print("%s is not a number!" % count)

class PushupMenu(InteractiveMenu):
    def title(self):
        return "Pushups"
    def main_loop(self):
        print("Count?")
        count = self.fancy_input()
        if count.isdigit():
            self.manager.insert_pushups(count)
        else:
            print("%s is not a number!" % count)

class BicepMenu(InteractiveMenu):
    def title(self):
        return "Biceps"
    def main_loop(self):
        print("Count?")
        count = self.fancy_input()
        if count.isdigit():
            self.manager.insert_biceps(count)
        else:
            print("%s is not a number!" % count) 

class PlankMenu(InteractiveMenu):
    def title(self):
        return "Planks"
    def main_loop(self):
        print("Seconds?")
        seconds = self.fancy_input()
        if seconds.isdigit():
            self.manager.insert_planks(seconds)
        else:
            print("%s is not a number!" % seconds)

class ShoulderMenu(InteractiveMenu):
    def title(self):
        return "Shoulders"
    def main_loop(self):
        print("Count?")
        count = self.fancy_input()
        if count.isdigit():
            self.manager.insert_shoulders(count)
        else:
            print("%s is not a number!" % count)

class LatsMenu(InteractiveMenu):
    def title(self):
        return "Lats"
    def main_loop(self):
        print("Count?")
        count = self.fancy_input()
        if count.isdigit():
            self.manager.insert_lats(count)
        else:
            print("%s is not a number!" % count)

class BikesMenu(InteractiveMenu):
    def title(self):
        return "Bikes"
    def main_loop(self):
        print("Seconds")
        count = self.fancy_input()
        if count.isdigit():
            self.manager.insert_bikes(count)
        else:
            print("%s is not a number!" % count)


