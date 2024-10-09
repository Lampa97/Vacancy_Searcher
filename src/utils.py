def range_vacancies_by_salary(vacancies: list, salary_range: str) -> list:
    """Filtering salaries according to given salary range"""
    min_salary, max_salary = list(map(int, salary_range.split('-')))
    return list(filter(lambda x: min_salary <= x.salary["from"] <= x.salary["to"] <= max_salary , vacancies))
