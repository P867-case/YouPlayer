import json


class Proccesing_file():
    def __init__(self, file: str='applicatio_data.json') -> None:
        """
            Обрабатывет json файл и позволяет: 
                получить
                записать
            данные в файл
        """
        self.file = file
        self.data = self.get_data()

    def get_data(self) -> dict:
        """Получит всё содержимое из файла и вернет его в формате dict"""
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        f.close()

        return data

    def update(self):
        """Обновит значение переменной data"""
        self.data = self.get_data()

    def save(self) -> bool:
        """Сохранит данные из перемнной data в файл"""
        with open(self.file, 'w', encoding='utf-8') as f:
            f.write(
                json.dumps(
                    self.data,
                    indent=4,
                    ensure_ascii=False
                )
            )
        return True
