"""Задание №2
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений."""

def func(some_dict: dict, key, default='Не найдено'):
    try:
        return some_dict[key]
    except KeyError:
        return default

if __name__ == '__main__':
    my_dict = {1: 'one'}
    print(func(my_dict, key=1 , default='no is it'))