shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма', 'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
print('Жанр для сериала Ведьмак:',shows['Ведьмак'])
# уместен for, так как пройдем по всем значениям, а для while необходимы условия прохождения, + больше кода
for i in shows.keys():
    print(i)
for j in shows.values():
    print(j)
