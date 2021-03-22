import pytest
from Task1.task1 import task1, task2, task3


class TestPosition:
    """ Tests for working with task1. """

    # Проверяет функцию task1
    def test_task1(self):
        assert task1('111111111111111111111111100000000') == 25

    @pytest.mark.parametrize('array,result', [('111111100000', 7), ('111111111111100000000000', 13)])
    def test_task1_1(self, array, result):
        assert task1(array) == result


    # Проверяет функцию task2
    def test_task2(self):
        assert task2('111111111111111111111111100000000') == 25

    @pytest.mark.parametrize('array,result', [('1111100000', 5), ('111111111100000000000', 10)])
    def test_task2_1(self, array, result):
        assert task2(array) == result


    # Проверяет функцию task3
    def test_task3(self):
        assert task3('111111111111111111111111100000000') == 25

    @pytest.mark.parametrize('array,result', [('11100000', 3), ('111111100000000000', 7)])
    def test_task3_1(self, array, result):
        assert task3(array) == result