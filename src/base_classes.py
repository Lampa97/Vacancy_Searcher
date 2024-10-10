from abc import ABC, abstractmethod

class BaseVacancyParser(ABC):
    """Abstract class for vacancy parsers"""

    @abstractmethod
    def fetch_vacancies(self, keyword):
        pass

    @abstractmethod
    def squeeze(self):
        pass

class BaseFileTool(ABC):
    """Abstract class for working with files"""

    @abstractmethod
    def save_all_to_file(self, vacancy_list):
        pass

    @abstractmethod
    def remove_from_file(self, number):
        pass