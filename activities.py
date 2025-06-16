import sqlite3 #TODO реализовать работу с бд

class Activities:
    def __init__(self, bd='activities.db' ):
        self.db_name = bd
        self.conn = None
        self._create_connection()
        self._create_table()

    # def __str__(self): #TODO вывод активностей реализовать
    #     for k,v in self.activities.items():
    #         print(v)
    #     return ''

    def _create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.conn.row_factory = sqlite3.Row
            print('Connected to database')
        except sqlite3.Error as e:
            self.conn = None
            print(e)

    def _create_table(self):
        if self.conn:
            try:
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
        else:
            print("Не удалось создать таблицу: нет соединения с БД.")

    def add(self, activity): #TODO Реализовать добавление активностей
        if self.conn:
            try:
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
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT rowid, * FROM activities")
                rows = cursor.fetchall()
                activities_list =[dict(row) for row in rows]
                for el in activities_list:
                    print(el)
            except sqlite3.Error as e:
                print(e)

    def remove(self, n): #TODO Удаление активности
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM activities WHERE rowid = (?)", (n,))
                self.conn.commit()
            except sqlite3.Error as e:
                print(e)
