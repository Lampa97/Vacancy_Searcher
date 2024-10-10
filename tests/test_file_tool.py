from src.file_tool import JsonFileTool
from src.vacancy import Vacancy


def test_init_jsonfiletool():
    json_saver = JsonFileTool("test_info")
    assert json_saver.filename == "test_info"
    assert json_saver.path == "data/test_info.json"


def test_save_all_to_file(vacancy_1, vacancy_2, vacancy_3):
    test_vacancy_list = [Vacancy(vacancy_1), Vacancy(vacancy_2), Vacancy(vacancy_3)]
    json_saver = JsonFileTool("test_info")
    json_saver.path = "tests/test_info.json"

    json_saver.save_all_to_file(test_vacancy_list)


def test_save_chosen_to_file(vacancies_list):
    json_saver = JsonFileTool("test_info")
    json_saver.path = "tests/test_info.json"

    json_saver.save_chosen_to_file(vacancies_list, [3, 4])


def test_remove_from_file():
    json_saver = JsonFileTool("test_info")
    json_saver.path = "tests/test_info.json"

    json_saver.remove_from_file([1])
