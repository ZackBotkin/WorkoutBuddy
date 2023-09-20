import datetime
from interactive_menu.src.interactive_menu import InteractiveMenu

class StatsMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)
        self.sub_menu_modules = [
            TotalStatsMenu(manager, self.path),
            PreviousStatsMenu(manager, self.path)
        ]

    def title(self):
        return "Stats"

class TotalStatsMenu(InteractiveMenu):

    def title(self):
        return "Total"

    def main_loop(self):
        ## { "pullups": .., "biceps": .. etc
        totals = self.manager.get_totals()
        print("")
        print("Totals")
        print("")
        for workout, total in totals.items():
            if workout in ['planks', 'bikes']:
                print("%s: %f minutes" % (workout, (total/60)))
            else:
                print("%s: %d reps" % (workout, total))
        print("")


class PreviousStatsMenu(InteractiveMenu):

    def title(self):
        return "Previous"

    def main_loop(self):

        print("How many days back?")
        days_back = self.fancy_input()

        ## TODO : this will error if not a number
        date = datetime.datetime.today() - datetime.timedelta(days=int(days_back))

        print("")
        print("Date: %s" % date)
        print("")
        totals = self.manager.get_totals(date)
        for workout, total in totals.items():
            if workout in ['planks']:
                print("%s: %f minutes" % (workout, (total/60)))
            else:
                print("%s: %d reps" % (workout, total))
        print("")



