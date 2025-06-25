from activities import *
from activity import *
import re


storage = Activities()

while True:
    try:
        com = int(input("Введите команду(-1 - Выйти, 0 - Печать всех активностей, 1 - Добавить, 2 - Удалить, 3 - Активности за день, 4 - Статистика за день: "))
        if com == -1:
            print("Выход")
            break
        elif com == 0:
            storage.show()
        elif com == 1:
            time = datetime.now().strftime('%d.%m.%Y')
            name = input("Введите название активности: ")
            type_of_activity = input("Введите тип активности: ")
            duration = int(input("Введите продолжительность активности(в минутах): "))
            act = Activity(time = time, name = name, type_of_activity=type_of_activity, duration=duration)
            storage.add(act)
            print(f'Добавлена активность {act}')
        elif com == 2:
            storage.show()
            n = int(input('Введите номер активности которую нужно удалить(-1 отмена): '))
            if n != -1:
                storage.remove(n)

        elif com == 3:
            storage.report()

        elif com == 4:
            dat = input("Введите дату формата 'дд.мм.гггг'(0 - если за сегодня): ")
            if dat == '0':
                storage.show_stats()
            else:
                storage.show_stats(dat)
        else:
            print('Invalid com!')

    except ValueError as e:
        print('Неверное значение', e)


def check_valid_date(dt):
    pattern = r'\d{2}\.\d{2}\.\d{4}'
    if re.match(pattern, dt):
        return True
    return False

def check_valid_name(nm):
    if isinstance(nm, str) and len(nm) in range(1, 21) and nm != ' ':
        return True
    return False

def check_valid_type(tp):
    if isinstance(tp, str) and len(tp) in range(1, 51) and tp != ' ':
        return True
    return False