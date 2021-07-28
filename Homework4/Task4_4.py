import random
shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма', 'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98, 'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}

movies = []



for key, value in shows.items():
    if value != 'фэнтази':
        if ratings[key] > 0.85:
            movies.append(key)

while True:
    gg = random.choice(movies)
    q = input('Сериал: ' + gg + ' , смотрим? Да или Нет:')
    if q == 'ДА' or q == 'да':
        break
    else:
        continue
