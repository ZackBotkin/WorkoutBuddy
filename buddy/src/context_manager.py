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

    def insert_bikes(self, seconds):
        query_runner = QueryRunner(self.config)
        query_runner.insert_bikes(datetime.now().strftime("%Y-%m-%d"), seconds)

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

        bikes_rows = query_runner.get_bikes(todays_date)
        bikes_seconds_total = 0
        for row in bikes_rows:
            bikes_seconds_total += row[1]
        print("\t%s minutes of bike kicks" % (bikes_seconds_total/60))

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

    def bar_graph_bikes(self):

        x_vals = []
        y_vals = []

        by_date = {}

        query_runner = QueryRunner(self.config)

        all_bikes_rows = query_runner.get_bikes()

        for row in all_bikes_rows:
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
        fig.write_html('bikes.html', auto_open=True)

    def consolidate_data(self, dry_run=True):

        query_runner = QueryRunner(self.config)

        total_pre_count = 0
        total_post_count = 0

        pullup_results = query_runner.consolidate_pullups(dry_run)
        total_pre_count += pullup_results["pre_count"]
        total_post_count += pullup_results["post_count"]

        pushup_results = query_runner.consolidate_pushups(dry_run)
        total_pre_count += pushup_results["pre_count"]
        total_post_count += pushup_results["post_count"]

        bicep_results = query_runner.consolidate_biceps(dry_run)
        total_pre_count += bicep_results["pre_count"]
        total_post_count += bicep_results["post_count"]

        plank_results = query_runner.consolidate_planks(dry_run)
        total_pre_count += plank_results["pre_count"]
        total_post_count += plank_results["post_count"]

        shoulder_results = query_runner.consolidate_shoulders(dry_run)
        total_pre_count += shoulder_results["pre_count"]
        total_post_count += shoulder_results["post_count"]

        lat_results = query_runner.consolidate_lats(dry_run)
        total_pre_count += lat_results["pre_count"]
        total_post_count += lat_results["post_count"]

        bikes_results = query_runner.consolidate_bikes(dry_run)
        total_pre_count += bikes_results["pre_count"]
        total_post_count += bikes_results["post_count"]

        consolidation_results = {
            "pullups": pullup_results,
            "pushups": pushup_results,
            "biceps": bicep_results,
            "planks": plank_results,
            "shoulders": shoulder_results,
            "lats": lat_results,
            "bikes": bikes_results,
            "total": {
                "pre_count": total_pre_count,
                "post_count": total_post_count
            }
        }

        return consolidation_results

    def get_totals(self, date=None):
        if date is not None:
            date = date.strftime("%Y-%m-%d")
        query_runner = QueryRunner(self.config)
        all_pullups = query_runner.get_pullups(date)
        all_pushups = query_runner.get_pushups(date)
        all_biceps = query_runner.get_biceps(date)
        all_planks = query_runner.get_planks(date)
        all_shoulders = query_runner.get_shoulders(date)
        all_lats = query_runner.get_lats(date)
        all_bikes = query_runner.get_bikes(date)
        return {
            "pullups": sum(int(v) for date, v in all_pullups),
            "pushups": sum(int(v) for date, v in all_pushups),
            "biceps": sum(int(v) for date, v in all_biceps),
            "planks": sum(int(v) for date, v in all_planks),
            "shoulders": sum(int(v) for date, v in all_shoulders),
            "lats": sum(int(v) for date, v in all_lats),
            "bikes": sum(int(v) for date, v in all_bikes),
        }


