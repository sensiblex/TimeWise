import datetime as tm

class Activity:
    def __init__(self, name="Без названия", activity="Общее", duration=1):
        self.time = tm.datetime.now().strftime("%d.%m.%Y")
        self.name = name
        self.type_of_activity = activity
        self.duration = duration

    def _is_valid_name(self, name):
        return isinstance(name, str) and len(name) > 0

    def _is_valid_duration(self, duration):
        return isinstance(duration, int) and duration > 0

    def _is_valid_type(self, type_of_activity):
        return isinstance(type_of_activity, str) and len(type_of_activity) > 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not self._is_valid_name(value):
            raise ValueError("Invalid name")
        self._name = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not self._is_valid_duration(value):
            raise ValueError("Invalid duration")
        self._duration = value

    @property
    def type_of_activity(self):
        return self._type_of_activity

    @type_of_activity.setter
    def type_of_activity(self, value):
        if not self._is_valid_type(value):
            raise ValueError("Invalid type")
        self._type_of_activity = value

    def __str__(self):
        return f"""Дата создания: {self.time}
Название: {self.name}
Тип активности: {self.type_of_activity}
Продолжительность: {self.duration}
        """

    def __eq__(self, other):
        return self.name == other.name
