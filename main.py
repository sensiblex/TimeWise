from activities import *
from activity import *


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
            name = input("Введите название активности: ")
            type_of_activity = input("Введите тип активности: ")
            duration = int(input("Введите продолжительность активности(в минутах): "))
            act = Activity(name, type_of_activity, duration)
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

    except ValueError:
        print('Неверное значение')