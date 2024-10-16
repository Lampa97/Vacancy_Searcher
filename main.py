import json
import re
from time import sleep

from src.file_tool import JsonFileTool
from src.hh_vacancies_fetcher import HeadHunterAPI
from src.logger import logger_setup
from src.utils import (
    filter_by_description,
    get_top_n_vacancies,
    print_vacancies,
    range_vacancies_by_salary,
    sort_vacancies,
)
from src.vacancy import Vacancy

main_logger = logger_setup()


def user_setup() -> dict:
    search_query = input("Please enter a keyword for vacancy search: \n")
    try:
        page_numbers = abs(
            int(input("Please enter a number of pages to search (each page contains 100 vacancies): \n"))
        )
        top_n = abs(int(input("Please enter a number of top N vacancies to receive: \n")))
    except ValueError:
        print("Invalid data. Values set to default. Number of pages: 20, top N vacancies: 5\n")
        page_numbers = 20
        top_n = 5
    filter_words = input(
        """Please enter a keywords for filtration by vacancy description (use space for separation)
         or press Enter to skip this step: \n"""
    ).split()
    salary_range = input(
        "Please enter salary range according to format (1000-2000). For single value type in format (2000-2000): \n"
    )
    if len(re.split("[,;-]", salary_range)) != 2 or not all(x.isdigit() for x in re.split("[,;-]", salary_range)):
        print("Invalid format. Salary range is set to default: 0-1000000\n")
        sleep(2)
        salary_range = "0-1000000"

    settings_info = {
        "search_query": search_query,
        "page_numbers": page_numbers,
        "top_n": top_n,
        "filter_words": filter_words,
        "salary_range": salary_range,
    }
    return settings_info


def working_with_vacancies(settings: dict) -> list:
    head_hunter_fetcher = HeadHunterAPI()
    head_hunter_fetcher.fetch_vacancies(settings["search_query"], settings["page_numbers"])
    formatted_vacancies = head_hunter_fetcher.squeeze()
    for vacancy in formatted_vacancies:
        one_vacancy = Vacancy(vacancy)
        Vacancy.cast_vacancies_to_list(one_vacancy)
    if settings["filter_words"]:
        filtered_vacancies = filter_by_description(Vacancy.vacancies_list, settings["filter_words"])
    else:
        filtered_vacancies = Vacancy.vacancies_list
    ranged_vacancies = range_vacancies_by_salary(filtered_vacancies, settings["salary_range"])
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_n_vacancies = get_top_n_vacancies(sorted_vacancies, settings["top_n"])
    return top_n_vacancies


def work_with_file(vacancies: list) -> None:
    filename_choice = input("Please type a name for json file (or leave empty for default name): \n")
    if filename_choice:
        json_handler = JsonFileTool(filename_choice)
    else:
        json_handler = JsonFileTool()
    method_choice = input(
        "If you want to save all vacancies, type 'all'. If you want to choose specific vacancies, type 'choose': \n"
    )
    if method_choice.lower() == "all":
        json_handler.save_all_to_file(vacancies)

    elif method_choice.lower() == "choose":
        user_choice = input(
            "Please choose index numbers of vacancies(separated by space or coma) you would like to save: \n"
        )
        index_choice = re.split("[,; ]", user_choice)
        index_numbers = list(map(int, index_choice))
        json_handler.save_chosen_to_file(vacancies, index_numbers)

    else:
        print("Invalid input. All vacancies will be saved.\n")
        json_handler.save_all_to_file(vacancies)

    delete_choice = input("Do you like to delete some vacancies from file? [y/n]: \n")
    if delete_choice.lower() in ["y", "yes", "yeah"]:
        with open(json_handler.path, "r", encoding="utf-8") as json_file:
            vacancies = json.load(json_file)
        for index, vacancy in enumerate(vacancies, 1):
            print(f"Vacancy #{index}\n {vacancy}")
        user_choice = input(
            "\nPlease choose index numbers of vacancies(separated by space or coma) you would like to delete: \n"
        )
        index_choice = re.split("[,; ]", user_choice)
        index_numbers = list(map(int, index_choice))
        json_handler.remove_from_file(index_numbers)
    else:
        print("Finished working with file\n")


def main_interaction() -> None:
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
        if file_choice.lower() in ["y", "yes", "yeah"]:
            work_with_file(user_vacancies)
        running_app = False

    print("Thank you!")
    input("\n\n\nPress Enter to exit.")


if __name__ == "__main__":
    main_interaction()
