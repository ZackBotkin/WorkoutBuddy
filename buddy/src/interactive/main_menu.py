from interactive_menu.src.interactive_menu import InteractiveMenu
from buddy.src.interactive.session_menu import SessionMenu
from buddy.src.interactive.list_menu import ListMenu
from buddy.src.interactive.sql_menu import SqlMenu
from buddy.src.interactive.graph_menu import GraphMenu
from buddy.src.interactive.goals_menu import GoalsMenu
from buddy.src.interactive.stats_menu import StatsMenu
from buddy.src.interactive.consolidate_menu import ConsolidateMenu

class MainMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)
        self.sub_menu_modules = [
            SessionMenu(manager, self.path),
            ListMenu(manager, self.path),
            StatsMenu(manager, self.path),
            GoalsMenu(manager, self.path),
            GraphMenu(manager, self.path),
            ConsolidateMenu(manager, self.path)
        ]
        if manager.config.get("enable_direct_sql_editing"):
            self.sub_menu_modules.append(SqlMenu(manager))

    def title(self):
        return "Main"
