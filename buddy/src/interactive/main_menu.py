from buddy.src.interactive.interactive_menu import InteractiveMenu
from buddy.src.interactive.session_menu import SessionMenu
from buddy.src.interactive.list_menu import ListMenu
from buddy.src.interactive.sql_menu import SqlMenu
from buddy.src.interactive.graph_menu import GraphMenu
from buddy.src.interactive.goals_menu import GoalsMenu
from buddy.src.interactive.stats_menu import StatsMenu

class MainMenu(InteractiveMenu):

    def __init__(self, manager):
        super().__init__(manager)
        self.sub_menu_modules = [
            SessionMenu(manager),
            ListMenu(manager),
            StatsMenu(manager),
            GoalsMenu(manager),
            GraphMenu(manager)
        ]
        if manager.config.get("enable_direct_sql_editing"):
            self.sub_menu_modules.append(SqlMenu(manager))
