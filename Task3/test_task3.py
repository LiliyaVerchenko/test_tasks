import requests
from Task3.task3 import appearance


tests = [
        {'data': {'lesson': [1594663200, 1594666800],
                  'pupil': [1594663340, 1594663389, 1594663390, 1594663395,
                            1594663396, 1594666472],
                  'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
         'answer': 3117
         },
        {'data': {'lesson': [1594702800, 1594706400],
                  'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                            1594704512, 1594704513, 1594704564, 1594705150,
                            1594704581, 1594704582, 1594704734, 1594705009,
                            1594705095, 1594705096, 1594705106, 1594706480,
                            1594705158, 1594705773, 1594705849, 1594706480,
                            1594706500, 1594706875, 1594706502, 1594706503,
                            1594706524, 1594706524, 1594706579, 1594706641],
                  'tutor': [1594700035, 1594700364, 1594702749, 1594705148,
                            1594705149, 1594706463]},
         'answer': 3577
         },
        {'data': {'lesson': [1594692000, 1594695600],
                  'pupil': [1594692033, 1594696347],
                  'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
         'answer': 3565
         },
    ]


def test_intervalsAPI():
    """ Tests for working API appearance(). """
    response = requests.get("http://127.0.0.1:5000/intervals/")
    assert response.status_code == 200
    assert response.headers.get("Content-Type") == "application/json"
    assert response.json()[0]['Case N1'] == "Expected 3117, Got 3117"
    assert len(response.json()) == 3
    assert response.json() == [
        {"Case N1": "Expected 3117, Got 3117"},
        {"Case N2": "Expected 3577, Got 3577"},
        {"Case N3": "Expected 3565, Got 3565"},
                                ]


def test_intervalsAPI_incorrect_path():
    """ Tests for working API appearance() with incorrect path. """
    response = requests.get("http://127.0.0.1:5000/")
    assert response.status_code == 404


def test_intervals():
    """ Tests for working appearance() with data of tests. """
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, ' \
                                              f'got {test_answer}, ' \
                                              f'expected {test["answer"]}'


def test_intervals_with_incorrect_data_in_tests():
    """ Tests for working appearance() with incorrect data in tests. """
    test = [
        {'data': {'lesson': [1594663200, 1594666800],
                  'pupil': [1594663340, 1594663385, 1594663390, 1594663395,
                            1594663396, 1594666472],
                  'tutor': [1594663400, 1594663430, 1594663443, 1594666473]},
         'answer': 3117
         }]
    for i, test in enumerate(test):
        test_answer = appearance(test['data'])
        assert test_answer != test['answer']
        assert AssertionError
