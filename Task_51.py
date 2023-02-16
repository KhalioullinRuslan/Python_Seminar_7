# Задача №51. 
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его.

# Ввод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print(‘same’)
# else:
#     print(‘different’)

# Вывод:
# same

values = [0, 2, 10, 6]

def same_by(characteristic, objects):
    # return len(set(map(characteristic, objects)))
    s = set([characteristic(x) for x in objects])
    if len(s) == 1:
        return True 
    else:
        return False

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')