для запуска теста нужно ввести:
python -m unittest 

test_3 не проходит, так как формат даты с '/' не должен проходить 

для вывода результата в html:
python -m pytest --cov . --cov-report html 

