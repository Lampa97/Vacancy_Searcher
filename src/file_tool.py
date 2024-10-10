from src.base_classes import BaseFileTool
import json

from src.vacancy import Vacancy


class JsonFileTool(BaseFileTool):
    """Class for working with vacancies in json file."""

    filename: str

    def __init__(self, filename):
        """Filename must be given without an extension. Extension '.json' will be added during initialization"""
        self.__filename = filename
        self.path = f"data/{self.__filename}.json"

    @property
    def filename(self):
        return self.__filename

    def save_all_to_file(self, vacancy_list: list):
        """Method rewriting or creating a new file with given vacancies"""
        ready_to_save = []
        for vacancy in vacancy_list:
            ready_to_save.append(vacancy.vacancy_info)
        with open(self.path, 'w', encoding='utf-8') as json_file:
            json.dump(ready_to_save, json_file, indent=4, ensure_ascii=False)

    def remove_from_file(self, numbers: list):
        """method removing a vacancy by a given list of index numbers"""
        with open(self.path, 'r', encoding='utf-8') as json_file:
            vacancies = json.load(json_file)
            for number in sorted(numbers, reverse=True):
                vacancies.pop(number)
        with open(self.path, 'w', encoding='utf-8') as json_file:
            json.dump(vacancies, json_file, indent=4, ensure_ascii=False)
