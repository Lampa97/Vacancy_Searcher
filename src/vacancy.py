class Vacancy:
    """Class for creating a vacancy object"""
    vacancy_info: dict

    vacancies_list = []

    def __init__(self, vacancy_info):
        self.name = vacancy_info.get('name')
        self.salary = vacancy_info.get('salary')
        self.url = vacancy_info.get('url')
        self.requirement = vacancy_info.get('requirement')

    def __len__(self):
        return len(self.vacancies_list)

    @classmethod
    def cast_vacancies_to_list(cls, vacancy):
        """Class method for adding vacancy to general list of vacancies"""
        cls.vacancies_list.append(vacancy)
