def filter_by_description(vacancies: list, filter_words: list) -> list:
    """Filtering vacancies by given filter words"""
    filtered_vacancies = []
    for vacancy in vacancies:
        for word in filter_words:
            if word.lower() in vacancy.requirement.lower():
                filtered_vacancies.append(vacancy)
                break
    return filtered_vacancies


def range_vacancies_by_salary(vacancies: list, salary_range: str) -> list:
    """Filtering salaries according to given salary range"""
    if vacancies:
        min_salary, max_salary = list(map(int, salary_range.split('-')))
        return list(filter(lambda x: min_salary <= x.salary["from"] <= x.salary["to"] <= max_salary , vacancies))
    return []
