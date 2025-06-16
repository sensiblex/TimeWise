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
                deadline TEXT
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
                __deadline = str(activity.deadline)
                cursor.execute("INSERT INTO activities (time, name, type_of_activity, deadline) VALUES (?, ?, ?, ?)", (__time, __name, __type_of_activity, __deadline))
                self.conn.commit()
            except sqlite3.Error as e:
                print(e)

    # def remove(self, n): #TODO Удаление активности
    #     del self.activities[n]
    #     temp = self.activities
    #     self.activities = {}
    #     ln = 1
    #     for k in temp.values():
    #         self.activities[ln] = k
    #         ln += 1
