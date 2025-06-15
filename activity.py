import datetime as tm

class Activity:

    def __init__(self, name=None, activity=None, duration=1, *args, **kwargs):
        """:parameter"""
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
    def __eq__(self, other):
        return self.name == other.name

# activities = Activity('123', 'sport', 2)
#
# print(activities)