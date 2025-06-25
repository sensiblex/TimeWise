import datetime as tm

from pydantic import BaseModel, field_validator

class Activity(BaseModel):
    time: str
    name: str
    type_of_activity: str
    duration: int

    

    @field_validator('time', mode='before')
    def parse_custom_date(cls, value):
        if isinstance(value, str):
            value = value.strip()
            try:
                return str(tm.datetime.strptime(value, '%d.%m.%Y').date().strftime('%d.%m.%Y'))

            except ValueError:
                raise ValueError('Invalid date, cant use this date')
        elif isinstance(value, tm.date):
            return value.strftime('%d.%m.%Y')
        raise ValueError('Invalid date, must be str or date class')

    @field_validator('name', mode='before')
    def parse_custom_name(cls, value):
        if isinstance(value, str):
            if len(value) > 0:
                return value
            raise ValueError('name cannot be empty')
        return str(value)

    @field_validator('type_of_activity', mode='before')
    def parse_custom_type_of_activity(cls, value):
        if isinstance(value, str):
            if len(value) > 0 and len(value) < 50:
                return value
            raise ValueError('type_of_activity cannot be empty and less than 50 characters')
        return str(value)

    @field_validator('duration', mode='before')
    def parse_custom_duration(cls, value):
        if isinstance(value, int):
            return value
        raise ValueError('duration must be an integer')

    def __str__(self):
        return f"""Дата создания: {self.time}
Название: {self.name}
Тип активности: {self.type_of_activity}
Продолжительность: {self.duration}
"""

    def __eq__(self, other):
        return self.name == other.name

# act = Activity(time='25.06.2025', name="sport", type_of_activity='sporting', duration=120)
