import requests
from Task2.task2 import get_animals_list, count_words


url1 = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%' \
        'D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%' \
        'D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8' \
        '%D1%82%D1%83'


test_data = ['Абботины', 'Абдера (жук)', 'Абелизавриды',
             'Абингдонская слоновая черепаха', 'Абиссинская сизоворонка',
             'Абиссинский заяц', 'Абиссинский рогатый ворон',
             'Абиссобротула', 'Абия прибайк']


def test_get_animals_list():
    """ Tests for working get_animals_list(). """
    resp = get_animals_list(url1)
    assert len(resp) == 200
    assert resp[0] == 'Абботины'


def test_count_words():
    """ Tests for working count_words() with test_data. """
    resp = count_words(test_data)
    assert type(resp) == str






