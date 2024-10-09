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

    @property
    def salary(self):
        return self.__salary

    def __len__(self):
        return len(self.vacancies_list)

    @classmethod
    def cast_vacancies_to_list(cls, vacancy):
        """Class method for adding vacancy to general list of vacancies"""
        cls.vacancies_list.append(vacancy)
