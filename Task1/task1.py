# 1 способ

def task1(array):
    """ Возвращает индекс первого нуля с помощью метода find(). """
    number_position = array.find('0')
    return number_position

print(task1('111111111111111111111111100000000'))


# 2 способ

def task2(array):
    """ Возвращает индекс первого нуля с помощью метода str.index(). """
    number_position = array.index('0')
    return number_position

print(task2('111111111111111111111111100000000'))


# 3 способ

def task3(array):
    """ Возвращает индекс первого нуля с помощью метода списка index(). """
    list_task = list(array)
    number_position = list_task.index('0')
    return number_position

print(task3('111111111111111111111111100000000'))
