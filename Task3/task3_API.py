import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/intervals/')
def appearance():
    """ Возвращает общее время присутствия ученика и
    учителя на уроке.

    """
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

    general_time = []
    for i, test in enumerate(tests):
        test_answer = test['data']

        # Получает множество секунд,
        # в течение которых длился урок.
        lesson = test_answer['lesson']
        lesson_list = []
        while len(lesson) > 0:
            start = lesson.pop(0)
            final = lesson.pop(0)
            for item in range(start, final):
                lesson_list.append(item)

        # Получает множество секунд, в течение
        # которых ученик присутствовал на уроке.
        pupil = test_answer['pupil']
        pupil_list = []
        while len(pupil) > 0:
            start = pupil.pop(0)
            final = pupil.pop(0)
            for item in range(start, final):
                pupil_list.append(item)

        # Получает множество секунд, в течение
        # которых учитель присутствовал на уроке.
        tutor = test_answer['tutor']
        tutor_list = []
        while len(tutor) > 0:
            start = tutor.pop(0)
            final = tutor.pop(0)
            for item in range(start, final):
                tutor_list.append(item)

        # Получает пересечение временных интервалов
        # урока, ученика и учителя.
        intersection = set(lesson_list).intersection(set(pupil_list),
                                                     set(tutor_list))

        if len(intersection) == test['answer']:
            result_of_case = {f'Case N{i+1}': f'Expected {test["answer"]}, '
                                              f'Got {len(intersection)}'}
            general_time.append(result_of_case)

    return jsonify(general_time)


if __name__ == '__main__':
    app.run(debug=True)
