import sqlite3

class QueryRunner(object):

    def __init__(self, config):
        self.config = config
        self.database_file_name = "%s\\%s.db" % (
            self.config.get("database_directory"),
            self.config.get("database_name")
        )

    def run_sql(self, sql_str):
        conn = sqlite3.connect(self.database_file_name)
        conn.execute(sql_str)
        conn.commit()

    def fetch_sql(self, sql_str):
        conn = sqlite3.connect(self.database_file_name)
        query = conn.execute(sql_str)
        results = query.fetchall()
        return results

    ##
    ##  Create table methods
    ##
    def create_tables(self):
        self.create_pullups_table()
        self.create_pushups_table()
        self.create_biceps_table()
        self.create_planks_table()
        self.create_shoulders_table()
        self.create_lats_table()
        self.create_bikes_table()

    def create_pullups_table(self):
        sql_str = "CREATE TABLE pullups(date DATE, count INT)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    def create_pushups_table(self):
        sql_str = "CREATE TABLE pushups(date DATE, count INT)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    def create_biceps_table(self):
        sql_str = "CREATE TABLE biceps(date DATE, count INT)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    def create_planks_table(self):
        sql_str = "CREATE TABLE planks(date DATE, seconds INT)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    def create_shoulders_table(self):
        sql_str = "CREATE TABLE shoulders(date DATE, count INT)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    def create_lats_table(self):
        sql_str = "CREATE TABLE lats(date DATE, count INT)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    def create_bikes_table(self):
        sql_str = "CREATE TABLE bikes(date DATE, seconds INT)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    ##
    ## Wipe table methods
    ##
    def wipe_all_tables(self):
        self.wipe_pullups_table()
        self.wipe_pushups_table()
        self.wipe_biceps_table()
        self.wipe_planks_table()
        self.wipe_shoulders_table()
        self.wipe_lats_table()
        self.wipe_bikes_table()

    def wipe_pullups_table(self):
        sql_str = "DELETE FROM pullups"
        self.run_sql(sql_str)

    def wipe_pushups_table(self):
        sql_str = "DELETE FROM pushups"
        self.run_sql(sql_str)

    def wipe_biceps_table(self):
        sql_str = "DELETE FROM biceps"
        self.run_sql(sql_str)

    def wipe_planks_table(self):
        sql_str = "DELETE FROM planks"
        self.run_sql(sql_str)

    def wipe_shoulders_table(self):
        sql_str = "DELETE FROM shoulders"
        self.run_sql(sql_str)

    def wipe_lats_table(self):
        sql_str = "DELETE FROM lats"
        self.run_sql(sql_str)

    def wipe_bikes_table(self):
        sql_str = "DELETE FROM bikes"
        self.run_sql(sql_str)

    ##
    ##  Get methods
    ##
    def get_pullups(self, date=None):
        sql_str = "SELECT * FROM pullups"
        if date is not None:
            sql_str += " WHERE date = '%s'" % date
        return self.fetch_sql(sql_str)

    def get_pushups(self, date=None):
        sql_str = "SELECT * FROM pushups"
        if date is not None:
            sql_str += " WHERE date = '%s'" % date
        return self.fetch_sql(sql_str)

    def get_biceps(self, date=None):
        sql_str = "SELECT * FROM biceps"
        if date is not None:
            sql_str += " WHERE date = '%s'" % date
        return self.fetch_sql(sql_str)

    def get_planks(self, date=None):
        sql_str = "SELECT * FROM planks"
        if date is not None:
            sql_str += " WHERE date = '%s'" % date
        return self.fetch_sql(sql_str)

    def get_shoulders(self, date=None):
        sql_str = "SELECT * FROM shoulders"
        if date is not None:
            sql_str += " WHERE date = '%s'" % date
        return self.fetch_sql(sql_str)

    def get_lats(self, date=None):
        sql_str = "SELECT * FROM lats"
        if date is not None:
            sql_str += " WHERE date = '%s'" % date
        return self.fetch_sql(sql_str)

    def get_bikes(self, date=None):
        sql_str = "SELECT * FROM bikes"
        if date is not None:
            sql_str += " WHERE date = '%s'" % date
        return self.fetch_sql(sql_str)

    ##
    ##  Insert methods
    ##
    def insert_pullups(self, date, count):
        sql_str = "INSERT INTO pullups ('date', 'count') VALUES ('%s', '%s')" % (date, count)
        self.run_sql(sql_str)

    def insert_pushups(self, date, count):
        sql_str = "INSERT INTO pushups ('date', 'count') VALUES ('%s', '%s')" % (date, count)
        self.run_sql(sql_str)

    def insert_biceps(self, date, count):
        sql_str = "INSERT INTO biceps ('date', 'count') VALUES ('%s', '%s')" % (date, count)
        self.run_sql(sql_str)

    def insert_planks(self, date, seconds):
        sql_str = "INSERT INTO planks ('date', 'seconds') VALUES ('%s', '%s')" % (date, seconds)
        self.run_sql(sql_str)

    def insert_shoulders(self, date, count):
        sql_str = "INSERT INTO shoulders ('date', 'count') VALUES ('%s', '%s')" % (date, count)
        self.run_sql(sql_str)

    def insert_lats(self, date, count):
        sql_str = "INSERT INTO lats ('date', 'count') VALUES ('%s', '%s')" % (date, count)
        self.run_sql(sql_str)

    def insert_bikes(self, date, seconds):
        sql_str = "INSERT INTO bikes ('date', 'seconds') VALUES ('%s', '%s')" % (date, seconds)
        self.run_sql(sql_str)

    #
    #   Consolidate data
    #
    def consolidate_pullups(self, dry_run=True):
        all_pullup_rows = self.get_pullups()
        seen_dates = {}
        row_count = 0
        for row in all_pullup_rows:
            row_count += 1
            date = row[0]
            count = row[1]
            if date not in seen_dates:
                seen_dates[date] = 0
            seen_dates[date] += count

        sql_str = "INSERT INTO pullups ('date', 'count') VALUES"
        for date, count in seen_dates.items():
            sql_str += "('%s', '%s')," % (date, count)
        sql_str = sql_str[:-1]

        if not dry_run:
            self.run_sql("DELETE FROM pullups")
            self.run_sql(sql_str)
        return {
            "pre_count": row_count,
            "post_count": len(seen_dates.keys())
        }

    def consolidate_pushups(self, dry_run=True):
        all_pushup_rows = self.get_pushups()
        seen_dates = {}
        row_count = 0
        for row in all_pushup_rows:
            row_count += 1
            date = row[0]
            count = row[1]
            if date not in seen_dates:
                seen_dates[date] = 0
            seen_dates[date] += count

        sql_str = "INSERT INTO pushups ('date', 'count') VALUES"
        for date, count in seen_dates.items():
            sql_str += "('%s', '%s')," % (date, count)
        sql_str = sql_str[:-1]

        if not dry_run:
            self.run_sql("DELETE FROM pushups")
            self.run_sql(sql_str)
        return {
            "pre_count": row_count,
            "post_count": len(seen_dates.keys())
        }

    def consolidate_biceps(self, dry_run=True):
        all_biceps_rows = self.get_biceps()
        seen_dates = {}
        row_count = 0
        for row in all_biceps_rows:
            row_count += 1
            date = row[0]
            count = row[1]
            if date not in seen_dates:
                seen_dates[date] = 0
            seen_dates[date] += count

        sql_str = "INSERT INTO biceps ('date', 'count') VALUES"
        for date, count in seen_dates.items():
            sql_str += "('%s', '%s')," % (date, count)
        sql_str = sql_str[:-1]

        if not dry_run:
            self.run_sql("DELETE FROM biceps")
            self.run_sql(sql_str)
        return {
            "pre_count": row_count,
            "post_count": len(seen_dates.keys())
        }

    def consolidate_planks(self, dry_run=True):
        all_planks_rows = self.get_planks()
        seen_dates = {}
        row_count = 0
        for row in all_planks_rows:
            row_count += 1
            date = row[0]
            count = row[1]
            if date not in seen_dates:
                seen_dates[date] = 0
            seen_dates[date] += count

        sql_str = "INSERT INTO planks ('date', 'seconds') VALUES"
        for date, seconds in seen_dates.items():
            sql_str += "('%s', '%s')," % (date, seconds)
        sql_str = sql_str[:-1]

        if not dry_run:
            self.run_sql("DELETE FROM planks")
            self.run_sql(sql_str)
        return {
            "pre_count": row_count,
            "post_count": len(seen_dates.keys())
        }

    def consolidate_shoulders(self, dry_run=True):
        all_shoulder_rows = self.get_shoulders()
        seen_dates = {}
        row_count = 0
        for row in all_shoulder_rows:
            row_count += 1
            date = row[0]
            count = row[1]
            if date not in seen_dates:
                seen_dates[date] = 0
            seen_dates[date] += count

        sql_str = "INSERT INTO shoulders ('date', 'count') VALUES"
        for date, count in seen_dates.items():
            sql_str += "('%s', '%s')," % (date, count)
        sql_str = sql_str[:-1]

        if not dry_run:
            self.run_sql("DELETE FROM shoulders")
            self.run_sql(sql_str)
        return {
            "pre_count": row_count,
            "post_count": len(seen_dates.keys())
        }

    def consolidate_lats(self, dry_run=True):
        all_lat_rows = self.get_lats()
        seen_dates = {}
        row_count = 0
        for row in all_lat_rows:
            row_count += 1
            date = row[0]
            count = row[1]
            if date not in seen_dates:
                seen_dates[date] = 0
            seen_dates[date] += count

        sql_str = "INSERT INTO lats ('date', 'count') VALUES"
        for date, count in seen_dates.items():
            sql_str += "('%s', '%s')," % (date, count)
        sql_str = sql_str[:-1]

        if not dry_run:
            self.run_sql("DELETE FROM lats")
            self.run_sql(sql_str)
        return {
            "pre_count": row_count,
            "post_count": len(seen_dates.keys())
        }

    def consolidate_bikes(self, dry_run=True):
        all_bikes_rows = self.get_bikes()
        seen_dates = {}
        row_count = 0
        for row in all_bikes_rows:
            row_count += 1
            date = row[0]
            count = row[1]
            if date not in seen_dates:
                seen_dates[date] = 0
            seen_dates[date] += count

        sql_str = "INSERT INTO bikes ('date', 'seconds') VALUES"
        for date, seconds in seen_dates.items():
            sql_str += "('%s', '%s')," % (date, seconds)
        sql_str = sql_str[:-1]

        if not dry_run:
            self.run_sql("DELETE FROM bikes")
            self.run_sql(sql_str)
        return {
            "pre_count": row_count,
            "post_count": len(seen_dates.keys())
        }

