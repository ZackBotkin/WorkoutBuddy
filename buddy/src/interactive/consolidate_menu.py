from interactive_menu.src.interactive_menu import InteractiveMenu


class ConsolidateMenu(InteractiveMenu):

    def title(self):
        return "Consolidate"


    def main_loop(self):
        print("Dry run? (will not actually change anything in the database)")
        answer = self.fancy_input()
        if answer in ["no", "No"]:
            dry_run = False
        else:
            dry_run = True
        results = self.manager.consolidate_data(dry_run)
        print("---------------------------------------------")
        if dry_run:
            print("| (DRY RUN, NO CHANGES TO DB COMMITED!!)")
            print("| ")
        print("| Pullups")
        print("|\tConsolidated %d rows to %d rows" % (results["pullups"]["pre_count"], results["pullups"]["post_count"]))
        print("| Pushups")
        print("|\tConsolidated %d rows to %d rows" % (results["pushups"]["pre_count"], results["pushups"]["post_count"]))
        print("| Biceps")
        print("|\tConsolidated %d rows to %d rows" % (results["biceps"]["pre_count"], results["biceps"]["post_count"]))
        print("| Planks")
        print("|\tConsolidated %d rows to %d rows" % (results["planks"]["pre_count"], results["planks"]["post_count"]))
        print("| Shoulders")
        print("|\tConsolidated %d rows to %d rows" % (results["shoulders"]["pre_count"], results["shoulders"]["post_count"]))
        print("| Lats")
        print("|\tConsolidated %d rows to %d rows" % (results["lats"]["pre_count"], results["lats"]["post_count"]))
        print("| Total")
        print("|\tConsolidated %d rows to %d rows" % (results["total"]["pre_count"], results["total"]["post_count"]))
        print("| ")
        print("|\tReduction of %d rows!" % (results["total"]["pre_count"] - results["total"]["post_count"]))
        print("---------------------------------------------")
