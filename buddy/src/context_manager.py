import plotly
import pandas
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


    ##
    ##  Graph functions, probably move to own class
    ##
    def bar_graph_pullups(self):

        x_vals = []
        y_vals = []

        by_date = {}

        query_runner = QueryRunner(self.config)

        all_pullup_rows = query_runner.get_pullups()

        for row in all_pullup_rows:
            date = row[0]
            count = row[1]
            if date not in by_date:
                by_date[date] = 0
            by_date[date] += count

        for date, count in by_date.items():
            x_vals.append(date)
            y_vals.append(count)

        import plotly.express as px
        df = pandas.DataFrame({
            'x': x_vals,
            'y': y_vals,
        })
        fig = px.bar(df, x='x', y='y')
        fig.write_html('pullups.html', auto_open=True)

    def bar_graph_pushups(self):

        x_vals = []
        y_vals = []

        by_date = {}

        query_runner = QueryRunner(self.config)

        all_pushup_rows = query_runner.get_pushups()

        for row in all_pushup_rows:
            date = row[0]
            count = row[1]
            if date not in by_date:
                by_date[date] = 0
            by_date[date] += count

        for date, count in by_date.items():
            x_vals.append(date)
            y_vals.append(count)

        import plotly.express as px
        df = pandas.DataFrame({
            'x': x_vals,
            'y': y_vals,
        })
        fig = px.bar(df, x='x', y='y')
        fig.write_html('pushups.html', auto_open=True)

    def bar_graph_biceps(self):

        x_vals = []
        y_vals = []

        by_date = {}

        query_runner = QueryRunner(self.config)

        all_bicep_rows = query_runner.get_biceps()

        for row in all_bicep_rows:
            date = row[0]
            count = row[1]
            if date not in by_date:
                by_date[date] = 0
            by_date[date] += count

        for date, count in by_date.items():
            x_vals.append(date)
            y_vals.append(count)

        import plotly.express as px
        df = pandas.DataFrame({
            'x': x_vals,
            'y': y_vals,
        })
        fig = px.bar(df, x='x', y='y')
        fig.write_html('biceps.html', auto_open=True)

    def bar_graph_planks(self):

        x_vals = []
        y_vals = []

        by_date = {}

        query_runner = QueryRunner(self.config)

        all_planks_rows = query_runner.get_planks()

        for row in all_planks_rows:
            date = row[0]
            count = row[1]
            if date not in by_date:
                by_date[date] = 0
            by_date[date] += count

        for date, count in by_date.items():
            x_vals.append(date)
            y_vals.append(count)

        import plotly.express as px
        df = pandas.DataFrame({
            'x': x_vals,
            'y': y_vals,
        })
        fig = px.bar(df, x='x', y='y')
        fig.write_html('planks.html', auto_open=True)

    def bar_graph_shoulders(self):

        x_vals = []
        y_vals = []

        by_date = {}

        query_runner = QueryRunner(self.config)

        all_shoulders_rows = query_runner.get_shoulders()

        for row in all_shoulders_rows:
            date = row[0]
            count = row[1]
            if date not in by_date:
                by_date[date] = 0
            by_date[date] += count

        for date, count in by_date.items():
            x_vals.append(date)
            y_vals.append(count)

        import plotly.express as px
        df = pandas.DataFrame({
            'x': x_vals,
            'y': y_vals,
        })
        fig = px.bar(df, x='x', y='y')
        fig.write_html('shoulders.html', auto_open=True)

    def bar_graph_lats(self):

        x_vals = []
        y_vals = []

        by_date = {}

        query_runner = QueryRunner(self.config)

        all_lats_rows = query_runner.get_lats()

        for row in all_lats_rows:
            date = row[0]
            count = row[1]
            if date not in by_date:
                by_date[date] = 0
            by_date[date] += count

        for date, count in by_date.items():
            x_vals.append(date)
            y_vals.append(count)

        import plotly.express as px
        df = pandas.DataFrame({
            'x': x_vals,
            'y': y_vals,
        })
        fig = px.bar(df, x='x', y='y')
        fig.write_html('lats.html', auto_open=True)

