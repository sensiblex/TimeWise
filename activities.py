import sqlite3 #TODO реализовать работу с бд

class Activities:
    def __init__(self, bd='activities.db' ):
        self.db_name = bd
        self.conn = None
        self._create_table()

    # def _create_connection(self):
    #     try:
    #         self.conn = sqlite3.connect(self.db_name)
    #         self.conn.row_factory = sqlite3.Row
    #         print('Connected to database')
    #     except sqlite3.Error as e:
    #         self.conn = None
    #         print(e)

    def _create_table(self):
        try:
            with sqlite3.connect(self.db_name) as self.conn:
                cursor = self.conn.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS activities (
                time TEXT,
                name TEXT,
                type_of_activity TEXT,
                duration TEXT
                )""")
                self.conn.commit()
                print('Table created successfully')
        except sqlite3.Error as e:
            print(e)

    def add(self, activity): #TODO Реализовать добавление активностей
        try:
            with sqlite3.connect(self.db_name) as self.conn:
                cursor = self.conn.cursor()
                __time = str(activity.time)
                __name = activity.name
                __type_of_activity = activity.type_of_activity
                __duration = str(activity.duration)
                cursor.execute("INSERT INTO activities (time, name, type_of_activity, duration) VALUES (?, ?, ?, ?)", (__time, __name, __type_of_activity, __duration))
                self.conn.commit()
        except sqlite3.Error as e:
            print(e)
    def show(self):
        try:
            with sqlite3.connect(self.db_name) as self.conn:
                self.conn.row_factory = sqlite3.Row
                cursor = self.conn.cursor()
                cursor.execute("SELECT rowid, * FROM activities")
                rows = cursor.fetchall()
                if rows:
                    activities_list =[dict(row) for row in rows]
                    for el in activities_list:
                        print(el)
                else:
                    print('Пустовато :(')

        except sqlite3.Error as e:
            print(e)
    def remove(self, n): #TODO Удаление активности
        try:
            with sqlite3.connect(self.db_name) as self.conn:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM activities WHERE rowid = (?)", (n,))
                self.conn.commit()
        except sqlite3.Error as e:
            print(e)