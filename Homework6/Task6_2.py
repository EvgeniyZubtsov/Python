shows = {
    'Секретные материалы':
        {'Жанр': 'фантастика', 'Рейтинг': 0.9},
    'Ведьмак':
        {'Жанр': 'фэнтази', 'Рейтинг': 0.95},
    'Клан Сопрано':
        {'Жанр': 'криминал', 'Рейтинг': 0.8},
    '24':
        {'Жанр': 'драма', 'Rating': 0.75},
    'Черное зеркало':
        {'Жанр': 'фантастика', 'Рейтинг': 0.98},
    'Во все тяжкие':
        {'Жанр': 'криминал', 'Рейтинг': 0.85},
    'Игра престолов':
        {'Жанр': 'фэнтази', 'Рейтинг': 0.87},
    'Карточный домик':
        {'Жанр': 'драма','Rating': 0.82},
    'Рик и Морти':
        {'Жанр': 'фантастика', 'Рейтинг': 1}
        }
janr = input("Введите жанр сериала: ")
search = []
for key,value in shows.items():
    for key_1,value_1 in value.items():
        if key_1 == 'Жанр':
            search.append(value_1)
print(set(search))

def search_informatioin(janr):
    count = 0
    for key,value in shows.items():
        for key_s, value_s in value.items():
            if value_s == janr:
                count +=1
    return (count)

print(search_informatioin(janr))