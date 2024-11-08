import os
import random
from Json_Api import Proccesing_file


class list_file_operation():
    """
    Класс для контролирования найденных файлов
    """

    def __init__(self):
        self.data_file = Proccesing_file('../applicatio_data.json')
        self.list_paths = self.data_file.data['default_path'] + self.data_file.data['paths']
        self.file_list = []

    def add_file_in_list(self, path_to_file: str):
        """
        добавит файл в список для отслживания
        path_to_file - абсолютный путь до файла
        """
        self.file_list.append(path_to_file)

    def scan(self):
        """Просканирует пути базовые и добавленые пользователем"""
        self.file_list = []
        for i in self.list_paths:
            for file in os.walk(i):
                try:
                    if '.mp3' in file[2][0]:
                        for i in file[2]:
                            if '.mp3' in f'{file[0]}/{i}':
                                self.add_file_in_list(f'{file[0]}/{i}')
                except IndexError:
                    pass

    def shuf(self, shuf_is_true: bool = True):
        """
        Перемищает файлы в списке
        shuf_is_true = False - вернет список в изначальное пложение
        """
        chas = []
        if shuf_is_true is True:
            count = len(self.file_list)
            for x in range(count):
                file = random.choice(self.file_list)
                chas.append(file)
                self.file_list.remove(file)

            self.file_list = chas
        elif shuf_is_true is False:
            self.scan()
