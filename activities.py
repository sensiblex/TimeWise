import sqlite3
from datetime import datetime
import logging
from tabulate import tabulate
logging.basicConfig(level=logging.DEBUG, filename='my_log.log', format='%(asctime)s - %(name)s - %(levelname)s - (%(lineno)d) [%(filename)s] - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode='a')
class Activities:
    def __init__(self, bd='activities.db' ):
        self.db_name = bd
        self._create_table()
        logging.debug('Activities table initialized')

    def _create_table(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS activities (
                time TEXT,
                name TEXT,
                type_of_activity TEXT,
                duration INTEGER
                )""")
                cursor.execute("""CREATE INDEX IF NOT EXISTS idx_time ON activities(time)""")
                conn.commit()
                logging.info("Table created successfully")
        except sqlite3.Error as e:
            logging.exception(e)

    def add(self, activity):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                time = activity.time
                name = activity.name
                type_of_activity = activity.type_of_activity
                duration = activity.duration
                cursor.execute("INSERT INTO activities (time, name, type_of_activity, duration) VALUES (?, ?, ?, ?)", (time, name, type_of_activity, duration))
                conn.commit()
                logging.info(f"Added activity successfully name: {name}, type: {type_of_activity}, duration: {duration}")
        except sqlite3.Error as e:
            logging.exception(e)

    def show(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT rowid, * FROM activities")
                rows = cursor.fetchall()
                if rows:
                    activities_list =[dict(row) for row in rows]
                    for el in activities_list:
                        print(el)
                    logging.info("Activities showed successfully")
                else:
                    print("No activities found")
                    logging.info("No activities found")
        except sqlite3.Error as e:
            logging.error(e, exc_info=True)

    def remove(self, n):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM activities WHERE rowid = (?)", (n,))
                if cursor.rowcount == 0:
                    print(f"No activity found with rowid: {n}")
                    logging.warning(f"No activities found with rowid: {n}")
                else:
                    print('Removed activity successfully')
                    logging.info(f"Removed activity successfully with rowid: {n}")
                conn.commit()
        except sqlite3.Error as e:
            logging.exception(e)

    def report(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                today_date = datetime.today().strftime('%d.%m.%Y')
                cursor.execute("SELECT time, name, type_of_activity, duration FROM activities WHERE time=?", (today_date,))
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                            print(*row)
                else:
                    print('There is no activity for today')
                    logging.info(f"No activities found for date: {today_date}")

        except sqlite3.Error as e:
            logging.exception(e)

    def show_stats(self, date=datetime.today().strftime('%d.%m.%Y')):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT time, type_of_activity, SUM(duration) FROM activities WHERE time = ? GROUP BY time, type_of_activity", (date,))
                rows = cursor.fetchall()
                headers = ['Дата', 'Тип активности', 'Общее время(минут)']
                if rows:
                    print(tabulate(rows, headers=headers, tablefmt='grid'))

                else:
                    print(f'За {date} пусто')
        except sqlite3.Error as e:
            logging.exception(e)


# conn = sqlite3.connect('activities.db')
# cursor = conn.cursor()
# cursor.execute("DROP TABLE activities")
# conn.commit()
# conn.close()
#
# act = Activities()
# # act.show()
# act.show_stats('24.06.2025')