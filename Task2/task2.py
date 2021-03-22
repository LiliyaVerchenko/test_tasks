import requests
from bs4 import BeautifulSoup


def get_animals_list(url):
    """ Возвращает список названий животных со страницы Википедии. """
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')
    list_animals_one_page = []
    resp = bs.find('div', id="mw-pages").find_all(
        'div', class_='mw-category-group')
    for i in resp:
        list_letter = i.findAll('a')
        for y in list_letter:
            title = y.get('title')
            list_animals_one_page.append(title)
    return list_animals_one_page


def count_words(list_animals):
    """ Возвращает количество слов на каждую букву алфавита. """
    # Создает списки для каждой буквы алфавита.
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_6 = []
    list_7 = []
    list_8 = []
    list_9 = []
    list_10 = []
    list_11 = []
    list_12 = []
    list_13 = []
    list_14 = []
    list_15 = []
    list_16 = []
    list_17 = []
    list_18 = []
    list_19 = []
    list_20 = []
    list_21 = []
    list_22 = []
    list_23 = []
    list_24 = []
    list_25 = []
    list_26 = []
    list_27 = []
    list_28 = []
    list_29 = []
    list_30 = []
    list_31 = []
    list_32 = []
    list_33 = []
    list_1en = []
    list_2en = []
    list_3en = []
    list_4en = []
    list_5en = []
    list_6en = []
    list_7en = []
    list_8en = []
    list_9en = []
    list_10en = []
    list_11en = []
    list_12en = []
    list_13en = []
    list_14en = []
    list_15en = []
    list_16en = []
    list_17en = []
    list_18en = []
    list_19en = []
    list_20en = []
    list_21en = []
    list_22en = []
    list_23en = []
    list_24en = []
    list_25en = []
    list_26en = []

    # Распределяет животных по спискам по первой букве
    # названия животного.
    for i in list_animals:
        if i[0] == 'А':
            list_1.append(i)
        elif i[0] == 'Б':
            list_2.append(i)
        elif i[0] == 'В':
            list_3.append(i)
        elif i[0] == 'Г':
            list_4.append(i)
        elif i[0] == 'Д':
            list_5.append(i)
        elif i[0] == 'Е':
            list_6.append(i)
        elif i[0] == 'Ё':
            list_7.append(i)
        elif i[0] == 'Ж':
            list_8.append(i)
        elif i[0] == 'З':
            list_9.append(i)
        elif i[0] == 'И':
            list_10.append(i)
        elif i[0] == 'Й':
            list_11.append(i)
        elif i[0] == 'К':
            list_12.append(i)
        elif i[0] == 'Л':
            list_13.append(i)
        elif i[0] == 'М':
            list_14.append(i)
        elif i[0] == 'Н':
            list_15.append(i)
        elif i[0] == 'О':
            list_16.append(i)
        elif i[0] == 'П':
            list_17.append(i)
        elif i[0] == 'Р':
            list_18.append(i)
        elif i[0] == 'С':
            list_19.append(i)
        elif i[0] == 'Т':
            list_20.append(i)
        elif i[0] == 'У':
            list_21.append(i)
        elif i[0] == 'Ф':
            list_22.append(i)
        elif i[0] == 'Х':
            list_23.append(i)
        elif i[0] == 'Ц':
            list_24.append(i)
        elif i[0] == 'Ч':
            list_25.append(i)
        elif i[0] == 'Ш':
            list_26.append(i)
        elif i[0] == 'Щ':
            list_27.append(i)
        elif i[0] == 'Ъ':
            list_28.append(i)
        elif i[0] == 'Ы':
            list_29.append(i)
        elif i[0] == 'Ь':
            list_30.append(i)
        elif i[0] == 'Э':
            list_31.append(i)
        elif i[0] == 'Ю':
            list_32.append(i)
        elif i[0] == 'Я':
            list_33.append(i)
        elif i[0] == 'A':
            list_1en.append(i)
        elif i[0] == 'B':
            list_2en.append(i)
        elif i[0] == 'C':
            list_3en.append(i)
        elif i[0] == 'D':
            list_4en.append(i)
        elif i[0] == 'E':
            list_5en.append(i)
        elif i[0] == 'F':
            list_6en.append(i)
        elif i[0] == 'G':
            list_7en.append(i)
        elif i[0] == 'H':
            list_8en.append(i)
        elif i[0] == 'I':
            list_9en.append(i)
        elif i[0] == 'J':
            list_10en.append(i)
        elif i[0] == 'K':
            list_11en.append(i)
        elif i[0] == 'L':
            list_12en.append(i)
        elif i[0] == 'M':
            list_13en.append(i)
        elif i[0] == 'N':
            list_14en.append(i)
        elif i[0] == 'O':
            list_15en.append(i)
        elif i[0] == 'P':
            list_16en.append(i)
        elif i[0] == 'Q':
            list_17en.append(i)
        elif i[0] == 'R':
            list_18en.append(i)
        elif i[0] == 'S':
            list_19en.append(i)
        elif i[0] == 'T':
            list_20en.append(i)
        elif i[0] == 'U':
            list_21en.append(i)
        elif i[0] == 'V':
            list_22en.append(i)
        elif i[0] == 'W':
            list_23en.append(i)
        elif i[0] == 'X':
            list_24en.append(i)
        elif i[0] == 'Y':
            list_25en.append(i)
        elif i[0] == 'Z':
            list_26en.append(i)

    return {'А': f'{len(list_1)}',
            'Б': f'{len(list_2)}',
            'В': f'{len(list_3)}',
            'Г': f'{len(list_4)}',
            'Д': f'{len(list_5)}',
            'Е': f'{len(list_6)}',
            'Ё': f'{len(list_7)}',
            'Ж': f'{len(list_8)}',
            'З': f'{len(list_9)}',
            'И': f'{len(list_10)}',
            'Й': f'{len(list_11)}',
            'К': f'{len(list_12)}',
            'Л': f'{len(list_13)}',
            'М': f'{len(list_14)}',
            'Н': f'{len(list_15)}',
            'О': f'{len(list_16)}',
            'П': f'{len(list_17)}',
            'Р': f'{len(list_18)}',
            'С': f'{len(list_19)}',
            'Т': f'{len(list_20)}',
            'У': f'{len(list_21)}',
            'Ф': f'{len(list_22)}',
            'Х': f'{len(list_23)}',
            'Ц': f'{len(list_24)}',
            'Ч': f'{len(list_25)}',
            'Ш': f'{len(list_26)}',
            'Щ': f'{len(list_27)}',
            'Ъ': f'{len(list_28)}',
            'Ы': f'{len(list_29)}',
            'Ь': f'{len(list_30)}',
            'Э': f'{len(list_31)}',
            'Ю': f'{len(list_32)}',
            'Я': f'{len(list_33)}',
            'A': f'{len(list_1en)}',
            'B': f'{len(list_2en)}',
            'C': f'{len(list_3en)}',
            'D': f'{len(list_4en)}',
            'E': f'{len(list_5en)}',
            'F': f'{len(list_6en)}',
            'G': f'{len(list_7en)}',
            'H': f'{len(list_8en)}',
            'I': f'{len(list_9en)}',
            'J': f'{len(list_10en)}',
            'K': f'{len(list_11en)}',
            'L': f'{len(list_12en)}',
            'M': f'{len(list_13en)}',
            'N': f'{len(list_14en)}',
            'O': f'{len(list_15en)}',
            'P': f'{len(list_16en)}',
            'Q': f'{len(list_17en)}',
            'R': f'{len(list_18en)}',
            'S': f'{len(list_19en)}',
            'T': f'{len(list_20en)}',
            'U': f'{len(list_21en)}',
            'V': f'{len(list_22en)}',
            'W': f'{len(list_23en)}',
            'X': f'{len(list_24en)}',
            'Y': f'{len(list_25en)}',
            'Z': f'{len(list_26en)}'
            }


if __name__ == '__main__':
    url1 = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%' \
           'D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%' \
           'D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8' \
           '%D1%82%D1%83'
    base_url = 'https://ru.wikipedia.org/'

    list_all_animals = []
    list_urls = [url1]

    # Цикл проходит по каждой страницу Википедии,
    # сохраняет животных в общий список,
    # и подсчитывает количество животных на каждую букву алфавита.
    while len(list_urls) > 0:
        list_urls = list_urls.pop(0)

        # Переходит на 'следующую' страницу
        response = requests.get(list_urls)
        bs = BeautifulSoup(response.text, 'html.parser')

        # Добавляет список с каждой страницы в общий список животных.
        list_all_animals += get_animals_list(list_urls)

        # Получает тег следующей страницы.
        next_page = bs.find('div', id="mw-pages").findAll('a')[-1]

        # Проверяет наличие следующей страницы,
        # создает ссылку и сохраняет ее в list_urls.
        # 1 варинт: Только русский алфавит.
        # if next_url_href and 'pagefrom=%' in next_url_href:

        # 2 вариант: Буквы русского и английского алфавитов.
        if next_page and 'Следующая' in str(next_page):
            next_url = base_url + next_page['href']
            list_urls = [next_url]
        else:
            break

    print(count_words(list_all_animals))

