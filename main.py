import manage
from activities import *
from activity import *

storage = Activities()
while True:
    try:
        com = int(input("Введите команду(0 - Печать всех активностей, 1 - добавить, 2 - переименовать, 3 - удалить: "))
        if com == 0:
            storage.show()
            pass
        elif com == 1:
            name = input("Введите название активности: ")
            type_of_activity = input("Введите тип активности: ")
            duration = int(input("Введите продолжительность активности(в минутах): "))
            act = Activity(name, type_of_activity, duration)
            storage.add(act)
            print(f'Добавлена активность {act}')

        elif com == 2:
            pass
        #     if storage.activities:
        #         for k, v in storage.activities.items():
        #             print(k, v.name)
        #         n = int(input('Введите номер активности у которой хотите поменять название: '))
        #         for k, v in storage.activities.items():
        #             if n == k:
        #                 print(f'Выбрана активность {v.name}')
        #                 new_name = input('Введите новое название: ')
        #                 manage.ManageActivity.rename(v, new_name)
        #                 print(f'Использовано новое имя {v.name}')
        #         else:
        #             print("Неверный номер активности")
        #     else:
        #         print('Список активностей пуст')
        #
        elif com == 3:
            storage.show()
            n = int(input('Введите номер активности которую нужно удалить: '))
            storage.remove(n)

    except ValueError:
        print('Неверное значение')

# noinspection PyUnreachableCode
storage.conn.close()