import datetime as tm
class Activity:

    def __init__(self, name=None, activity=None, duration=1):
        self.time = tm.datetime.now().strftime("%d.%m.%Y")
        self.name = name
        self.type_of_activity = activity
        self.duration = duration

    def __str__(self):
        return str(f"""Дата создания: {self.time}
Название: {self.name}
Тип активности: {self.type_of_activity}
Продолжительность: {self.duration}
        """)
    def __eq__(self, other):
        return self.name == other.name