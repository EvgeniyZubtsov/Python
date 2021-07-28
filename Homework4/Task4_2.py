anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Секретные материалы': 'фантастика','Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика',}

# Создаем списки из ключей для последующего сравнения и переводим их в множества
list_anya = set(anya.keys())
list_olya = set(olya.keys())
list_nastya = set(nastya.keys())
list_sveta = set(sveta.keys())
# Сравниваем с кем из коллег у Ани больше всего общих любимых сериалов, с помощью len вычисляем количество
olya_count = len(list_anya & list_olya)
nastya_count = len(list_anya & list_nastya)
sveta_count = len(list_anya & list_sveta)

# Создаем новый список с именами и количеством пересечений
list_interesting = {
    "Олей": olya_count,
    "Настей" : nastya_count,
    "Светой" : sveta_count
}
name = ''
name2 = ''
max_interesting = 0
list_add = []
for key,value in list_interesting.items():
    if list_interesting[key] > max_interesting:
        max_interesting = list_interesting[key]
        name = key
    elif list_interesting[key] == max_interesting and max_interesting !=0:
        max_interesting = list_interesting[key]
        name2 = key
        list_add.append(f'Больше всего общих сериалов с {name} и {name2}')
if len(list_add)!= 0:
    for elem in list_add:
        print(elem)
else:
    print('Больше всех имеет совпадений',name)