import pytest
from src.vacancy import Vacancy
from src.hh_vacancies_fetcher import HeadHunterAPI
from src.file_tool import JsonFileTool

@pytest.fixture
def vacancy_1():
    return {'name': 'Python developer', 'salary': {'from': 100, 'to': 300, 'currency': 'RUR'}, 'url': 'test_url', 'requirement': 'SQL'}

@pytest.fixture
def vacancy_2():
    return {'name': 'Java developer', 'salary': {'from': None, 'to': 300, 'currency': 'RUR'}, 'url': 'test_url', 'requirement': 'Java'}

@pytest.fixture
def vacancy_3():
    return {'name': 'DevOps', 'salary': {'from': 100, 'to': None, 'currency': 'RUR'}, 'url': 'test_url', 'requirement': 'Management skills'}

@pytest.fixture
def vacancy_4():
    return {'name': 'Senior Python developer', 'salary': {'from': 400, 'to': 600, 'currency': 'RUR'}, 'url': 'test_url', 'requirement': 'SQL'}

@pytest.fixture
def vacancy_5():
    return {'name': 'C++ developer', 'salary': {'from': 300, 'to': 400, 'currency': 'RUR'}, 'url': 'test_url', 'requirement': None}

@pytest.fixture
def vacancies_list(vacancy_1, vacancy_2, vacancy_3, vacancy_4, vacancy_5):
    return [Vacancy(vacancy_1), Vacancy(vacancy_2), Vacancy(vacancy_3), Vacancy(vacancy_4), Vacancy(vacancy_5)]