from time import sleep
import json
import re
from src.hh_vacancies_fetcher import HeadHunterAPI
from src.vacancy import Vacancy
from src.file_tool import JsonFileTool
from src.logger import logger_setup
from src.utils import (
    filter_by_description,
    sort_vacancies,
    range_vacancies_by_salary,
    get_top_n_vacancies,
    print_vacancies,
)


main_logger = logger_setup()


def user_setup():
    search_query = input("Please enter a keyword for vacancy search: \n")
    try:
        page_numbers = abs(int(input("Please enter a number of pages to search (each page contains 100 vacancies): \n")))
        top_n = abs(int(input("Please enter a number of top N vacancies to receive: \n")))
    except ValueError:
        print("Invalid data. Values set to default. Number of pages: 20, top N vacancies: 5\n")
        page_numbers = 20
        top_n = 5
    filter_words = input(
        "Please enter a keywords for filtration by vacancy description (use space for separation): \n"
    ).split()
    salary_range = input("Please enter salary range according to format (1000-2000): \n")
    if len(salary_range.split("-")) > 2 and not all(x.isdigit() for x in salary_range.split("-")):
        print("Invalid format. Salary range is set to default: 0-1000000\n")
        salary_range = ["0", "1000000"]

    settings_info = {
        "search_query": search_query,
        "page_numbers": page_numbers,
        "top_n": top_n,
        "filter_words": filter_words,
        "salary_range": salary_range,
    }
    return settings_info


def working_with_vacancies(settings):
    head_hunter_fetcher = HeadHunterAPI()
    head_hunter_fetcher.fetch_vacancies(settings["search_query"], settings["page_numbers"])
    formatted_vacancies = head_hunter_fetcher.squeeze()
    for vacancy in formatted_vacancies:
        one_vacancy = Vacancy(vacancy)
        Vacancy.cast_vacancies_to_list(one_vacancy)
    filtered_vacancies = filter_by_description(Vacancy.vacancies_list, settings["filter_words"])
    ranged_vacancies = range_vacancies_by_salary(filtered_vacancies, settings["salary_range"])
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_n_vacancies = get_top_n_vacancies(sorted_vacancies, settings["top_n"])
    return top_n_vacancies

def work_with_file(vacancies):
    filename_choice = input("Please type a name for json file: \n")
    json_handler = JsonFileTool(filename_choice)
    method_choice = input(
        "If you want to save all vacancies, type 'all'. If you want to choose specific vacancies, type 'choose': \n")
    if method_choice.lower() == 'all':
        json_handler.save_all_to_file(vacancies)

    elif method_choice.lower() == 'choose':
        indexes_choice = input('Please choose index numbers of vacancies(separated by space or coma) you would like to save: \n')
        index_numbers = re.split('[,; ]', indexes_choice)
        json_handler.save_chosen_to_file(vacancies, index_numbers)

    else:
        print("Invalid input. All vacancies will be saved.\n")
        json_handler.save_all_to_file(vacancies)

    delete_choice = input('Do you like to delete some vacancies from file? [y/n]: \n')
    if delete_choice in ['y', 'yes', 'yeah']:
        with open(json_handler.path, "r", encoding="utf-8") as json_file:
            vacancies = json.load(json_file)
        print_vacancies(vacancies)
        indexes_choice = input(
            'Please choose index numbers of vacancies(separated by space or coma) you would like to delete: \n')
        index_numbers = re.split('[,; ]', indexes_choice)
        json_handler.remove_from_file(index_numbers)
    else:
        print('Finished working with file\n')

def main_interaction():
    running_app = True
    while running_app:
        print("Welcome to 'Vacancy Searcher App'!\n Let's setup your search tool first\n")
        sleep(2)

        user_settings = user_setup()
        print("Searching tool set up. Please wait\n")
        sleep(2)

        user_vacancies = working_with_vacancies(user_settings)
        print("Printing vacancies to console\n")
        sleep(2)

        print_vacancies(user_vacancies)
        file_choice = input("Do you want to save vacancies to file? [y/n]: \n")
        if file_choice in ['y', 'yes', 'yeah']:
            work_with_file(user_vacancies)
        running_app = False

    print('Thank you!')
    input('\n\n\nPress Enter to exit.')


if __name__ == "__main__":
    main_interaction()