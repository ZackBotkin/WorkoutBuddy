from datetime import datetime
from buddy.src.io.query_runner import QueryRunner

class ContextManager(object):

    def __init__(self, configs):
        self.config = configs

    def insert_pullups(self, count):
        query_runner = QueryRunner(self.config)
        query_runner.insert_pullups(datetime.now().strftime("%Y-%m-%d"), count)

    def insert_pushups(self, count):
        query_runner = QueryRunner(self.config)
        query_runner.insert_pushups(datetime.now().strftime("%Y-%m-%d"), count)

    def insert_biceps(self, count):
        query_runner = QueryRunner(self.config)
        query_runner.insert_biceps(datetime.now().strftime("%Y-%m-%d"), count)

    def insert_planks(self, seconds):
        query_runner = QueryRunner(self.config)
        query_runner.insert_planks(datetime.now().strftime("%Y-%m-%d"), seconds)

    def insert_shoulders(self, count):
        query_runner = QueryRunner(self.config)
        query_runner.insert_shoulders(datetime.now().strftime("%Y-%m-%d"), count)

    def insert_lats(self, count):
        query_runner = QueryRunner(self.config)
        query_runner.insert_lats(datetime.now().strftime("%Y-%m-%d"), count)

    def print_todays_workouts(self):

        query_runner = QueryRunner(self.config)

        todays_date = datetime.now().strftime("%Y-%m-%d")

        print("-----------------------------------")
        print("Workout for %s" % todays_date)
        print(" ")

        pullup_rows = query_runner.get_pullups(todays_date)
        pullup_total = 0
        for row in pullup_rows:
            pullup_total += row[1]
        print("\t%d pullups" % pullup_total)

        pushup_rows = query_runner.get_pushups(todays_date)
        pushup_total = 0
        for row in pushup_rows:
            pushup_total += row[1]
        print("\t%d pushups" % pushup_total)

        bicep_rows = query_runner.get_biceps(todays_date)
        bicep_total = 0
        for row in bicep_rows:
            bicep_total += row[1]
        print("\t%d bicep curls" % bicep_total)

        plank_rows = query_runner.get_planks(todays_date)
        plank_seconds_total = 0
        for row in plank_rows:
            plank_seconds_total += row[1]
        print("\t%s minutes of planks" % (plank_seconds_total/60))

        shoulder_rows = query_runner.get_shoulders(todays_date)
        shoulder_total = 0
        for row in shoulder_rows:
            shoulder_total += row[1]
        print("\t%d shoulder raises" % shoulder_total)

        lat_rows = query_runner.get_lats(todays_date)
        lats_total = 0
        for row in lat_rows:
            lats_total += row[1]
        print("\t%d lat raises" % lats_total)

        print("-----------------------------------")

