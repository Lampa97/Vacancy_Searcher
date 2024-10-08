from abc import ABC, abstractmethod

class BaseVacancyParser(ABC):
    """Abstract class for vacancy parsers"""

    @abstractmethod
    def fetch_vacancies(self, keyword):
        pass