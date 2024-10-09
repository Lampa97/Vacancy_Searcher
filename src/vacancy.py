class Vacancy:
    """Class for creating a vacancy object"""
    vacancy_info: dict

    vacancies_list = []
    vacancy_id = 0

    def __init__(self, vacancy_info):
        self.__name = vacancy_info.get('name')
        self.__salary = vacancy_info.get('salary')
        self.__url = vacancy_info.get('url')
        self.__requirement = vacancy_info.get('requirement')
        self.id = self.vacancy_id
        self.vacancy_id += 1
        if self.__salary['to'] is None:
            self.__salary['to'] = self.__salary['from']
        if self.__salary['from'] is None:
            self.__salary['from'] = self.__salary['to']

    @property
    def salary(self):
        return self.__salary

    def __gt__(self, other):
        if type(self) is type(other):
            return self.salary['to'] > other.salary['to']

    def __lt__(self, other):
        if type(self) is type(other):
            return self.salary['to'] < other.salary['to']

    def __ge__(self, other):
        if type(self) is type(other):
            return self.salary['to'] >= other.salary['to']

    def __le__(self, other):
        if type(self) is type(other):
            return self.salary['to'] <= other.salary['to']

    def __len__(self):
        return len(self.vacancies_list)

    @classmethod
    def cast_vacancies_to_list(cls, vacancy):
        """Class method for adding vacancy to general list of vacancies"""
        cls.vacancies_list.append(vacancy)
