# Vacancy_Searcher
This application provides a tools for searching, filtering and sorting the vacancies using different API.
App allows to save data to file, read data and remove specific vacancies.

## Program functionality

1. *base_classes* - module with defined abstract classes. (For API parser and File tools).
2. *file_tool* - class **JSONFileTool**. When initializing taking a filename as an argument (default parameter - 'vacancy').
Allows to read json file, save all or chosen data or delete chosen data from file.
3. *hh_vacancies_fetcher* - class **HeadHunterAPI** is a class which is working only with HeadHunter API for getting vacancies by a keyword.
Additional method *squeeze* for filtering only valuable information about vacancy.
4. *vacancy* - class **Vacancy** for initialization of vacancy object. Supports comparing between vacancies by salary.
During initialization - if vacancy missing one of the salary attribute - setting it to *0*. 
Allows to add vacancy to general list of vacancies on the class level. 
5. *utils* - functions for working with vacancies - filtering, sorting, ranging by salary, getting top N and printing in readable format.

### How program works

While running, program will ask user about information needed to search required vacancies.
User may either save all vacancies to file or choose only specific vacancies by giving vacancy id number.
If vacancy was added by mistake it's still possible to delete it.

#### Reminder
* If user left salary range empty - default salary range will be set (0-100000).
* Please strictly follow instruction given by program to get desired results.
* File will be saved to *data* directory. Please don't remove this folder.



Project using virtual environment ***Poetry***. Information about dependencies
located in ***pyproject.toml***. 

For smooth installation of dependencies recommended to use ***Poetry*** virtual environment. 

To install dependencies use command:

```
poetry install
```


### Информация о тестировании проекта:

Application using ***pytest*** as a testing framework.

You can find information about tests coverage in directory ***htmlcov***.

For running tests use command:

```
pytest
```
