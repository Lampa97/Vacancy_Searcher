from src.base_classes import BaseFileTool
import json


class JsonFileTool(BaseFileTool):
    """Class for working with vacancies in json file."""

    filename: str

    def __init__(self, filename):
        """Filename must be given without an extension. Extension '.json' will be added during initialization"""
        self.__filename = filename
        self.path = f"../data/{self.filename}.json"

    def save_all_to_file(self, vacancy_list: list):
        """Method rewriting or creating a new file with given vacancies"""
        with open(self.path, 'w', encoding='utf-8') as json_file:
            json.dump(vacancy_list, json_file, indent=4, ensure_ascii=False)

    def save_one_to_file(self, vacancy: dict):
        """Method adding one vacancy to the file"""
        with open(self.path, 'a', encoding='utf-8') as json_file:
            json.dump(vacancy, json_file, indent=4, ensure_ascii=False)


    def remove_from_file(self, numbers: list):
        """method removing a vacancy by a given list of index numbers"""
        with open(self.path, 'r', encoding='utf-8') as json_file:
            vacancies = json.load(json_file)
            for number in sorted(numbers, reverse=True):
                vacancies.pop(number)
        with open(self.path, 'w', encoding='utf-8') as json_file:
            json.dump(vacancies, json_file, indent=4, ensure_ascii=False)
