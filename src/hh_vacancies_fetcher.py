import requests
from src.base_classes import BaseVacancyParser
from src.logger import logger_setup
from src.vacancy import Vacancy
from src.file_tool import JsonFileTool
from src.utils import range_vacancies_by_salary

api_logger = logger_setup()


class HeadHunterAPI(BaseVacancyParser):
    """Class-connector to hh.ru API for getting vacancies by keyword"""

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []


    def fetch_vacancies(self, keyword: str):
        self.__params['text'] = keyword
        while self.__params['page'] != 5:
            api_logger.info(f'Parsing page number: {self.__params['page']}')
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                api_logger.info('Vacancies successfully added to list')
            self.__params['page'] += 1


    def squeeze(self) -> list:
        """Choosing only useful information from api response and returning filtered list with salary in RUB"""
        squeezed_info = []
        for vacancy in self.vacancies:
            try:
                if vacancy.get('salary').get('currency') == 'RUR':
                    current_vacancy = dict()
                    current_vacancy['name'] = vacancy['name']
                    current_vacancy['salary']= vacancy.get('salary')
                    current_vacancy['url'] = vacancy['alternate_url']
                    current_vacancy['requirement'] = vacancy['snippet'].get('requirement')
                    del current_vacancy['salary']['gross']
                    squeezed_info.append(current_vacancy)
            except AttributeError:
                continue
        return squeezed_info





my_json = JsonFileTool('filer')


hh = HeadHunterAPI()

hh.fetch_vacancies('python')

print(hh.vacancies)


my = hh.squeeze()

print(my)



for vacancy in my:
    new_vac = Vacancy(vacancy)
    Vacancy.cast_vacancies_to_list(new_vac)

print(Vacancy.vacancies_list)

lll = Vacancy.vacancies_list

ooo = range_vacancies_by_salary(lll, '80000-120000')

for i in lll:
    print(i.salary)

for i in ooo:
    print(i.salary)

# print(lll[2] >= lll[1])
# print(lll[2])
# print(lll[1])
#
# sss = sorted(lll, reverse=True)
#
# print(lll[2].vacancy_info)
#
# ff = JsonFileTool('files')
#
# ff.save_all_to_file(sss)