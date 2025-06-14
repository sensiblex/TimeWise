import datetime as tm

class Activities:
    def __init__(self, name, activity):
        self.time = tm.datetime.now()
        self.name = name

        self.type_of_activity = activity
    def __str__(self):
        return str(f"""Дата создания: {self.time}
Название: {self.name}
        """)


activities = Activities('123', 'sport')


print(activities)
