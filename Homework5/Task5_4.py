# -*- coding: cp1251 -*-
filename = 'dnevnik.txt'
guess = input('Напишите дату и введите краткую запись о событиях на эту дату: ')
with open(filename, 'a') as file:
    file.write("\n" + guess)

with open(filename) as file:
    content = file.read()
    print(content)

