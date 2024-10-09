from src.utils import filter_by_description, range_vacancies_by_salary, get_top_n_vacancies, sort_vacancies


def test_filter_by_description(vacancies_list):
    filtered_vacancies = filter_by_description(vacancies_list, ['SQL', 'Java'])
    assert len(filtered_vacancies) == 3


def test_range_vacancies_by_salary(vacancies_list):
    ranged_vacancies = range_vacancies_by_salary(vacancies_list, '300-600')
    assert ranged_vacancies[0].salary == {'from': 400, 'to': 600, 'currency': 'RUR'}
    assert ranged_vacancies[1].salary == {'from': 300, 'to': 400, 'currency': 'RUR'}

def test_range_vacancies_by_salary_empty():
    assert range_vacancies_by_salary([], '100-500') == []

def test_get_top_3_vacancies(vacancies_list):
    top_3 = get_top_n_vacancies(vacancies_list, 3)
    assert len(top_3) == 3

def test_get_top_n_vacancies_more(vacancies_list):
    top_n = get_top_n_vacancies(vacancies_list, 7)
    assert len(top_n) == 5

def test_sort_vacancies(vacancies_list):
    sorted_vacancies = sort_vacancies(vacancies_list)
    assert sorted_vacancies[0].salary == {'from': 400, 'to': 600, 'currency': 'RUR'}
    assert sorted_vacancies[-1].salary == {'from': 100, 'to': 0, 'currency': 'RUR'}