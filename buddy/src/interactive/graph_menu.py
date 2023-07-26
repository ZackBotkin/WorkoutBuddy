from interactive_menu.src.interactive_menu import InteractiveMenu

class GraphMenu(InteractiveMenu):

    def __init__(self, manager):
        super().__init__(manager)
        self.sub_menu_modules = [
            GraphAllMenu(manager),
            GraphPullupsMenu(manager),
            GraphPushupsMenu(manager),
            GraphBicepsMenu(manager),
            GraphPlanksMenu(manager),
            GraphShouldersMenu(manager),
            GraphLatsMenu(manager)
        ]

    def title(self):
        return "Graphs"

class GraphAllMenu(InteractiveMenu):

    def title(self):
        return "All"

    def main_loop(self):
        self.manager.bar_graph_pullups()
        self.manager.bar_graph_pushups()
        self.manager.bar_graph_biceps()
        self.manager.bar_graph_planks()
        self.manager.bar_graph_shoulders()
        self.manager.bar_graph_lats()

class GraphPullupsMenu(InteractiveMenu):

    def title(self):
        return "Pullups"

    def main_loop(self):
        self.manager.bar_graph_pullups()

class GraphPushupsMenu(InteractiveMenu):

    def title(self):
        return "Pushups"

    def main_loop(self):
        self.manager.bar_graph_pushups()

class GraphBicepsMenu(InteractiveMenu):

    def title(self):
        return "Biceps"

    def main_loop(self):
        self.manager.bar_graph_biceps()

class GraphPlanksMenu(InteractiveMenu):

    def title(self):
        return "Planks"

    def main_loop(self):
        self.manager.bar_graph_planks()

class GraphShouldersMenu(InteractiveMenu):

    def title(self):
        return "Shoulders"

    def main_loop(self):
        self.manager.bar_graph_shoulders()

class GraphLatsMenu(InteractiveMenu):

    def title(self):
        return "Lats"

    def main_loop(self):
        self.manager.bar_graph_lats()

