import datetime as tm

class Activities:
    def __init__(self, name, activity, duration):
        self.time = tm.datetime.now()
        self.name = name
        self.type_of_activity = activity
        self.deadline = tm.datetime.now()+ tm.timedelta(hours=duration)
    def __str__(self):
        return str(f"""Дата создания: {self.time}
Название: {self.name}
Тип активности: {self.type_of_activity}
Дедлайн: {self.deadline}
        """)


activities = Activities('123', 'sport', 2)


print(activities)
