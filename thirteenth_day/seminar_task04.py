"""
Задание №4
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""

import os
import json

class User:
    def __init__(self, name: str, the_id: int, level: int):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError('Name must be a string.')
        self.name = name
        if not isinstance(the_id, int) or the_id <= 0 :
            raise ValueError('id must be an integer greater than zero')
        self.the_id = the_id
        if not isinstance(level, int) or level not in range(1, 8):
            raise ValueError('level must be a integer from 1 to 7')
        self.level = level

    def __str__(self):
        return f'{self.name = }, {self.the_id = }, {self.level = }'

def load_json(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
    else:
        data = {}
    return data


def worker():

    while True:
        try:
            name = input('Enter name: ')
            the_id = int(input('Enter ID: '))
            level = int(input('Enter level (1-7): '))
            return User(name, the_id, level)
        except ValueError as e:
            print(e)


def save_json(path, user_db):
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(user_db, file, indent=4, ensure_ascii=False)



if __name__ == '__main__':
    path = 'my_json.json'
    user_db = load_json(path)
    new_user = worker()
    if str(new_user.the_id) in user_db:
        raise Exception('Пользователь c таким iD уже есть в базе')
    else:
        user_db[new_user.the_id] = (new_user.name, new_user.level)
        save_json(path, user_db)







