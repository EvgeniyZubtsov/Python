# -*- coding: cp1251 -*-
filename = 'dnevnik.txt'
guess = input('�������� ���� � ������� ������� ������ � �������� �� ��� ����: ')
with open(filename, 'a') as file:
    file.write("\n" + guess)

with open(filename) as file:
    content = file.read()
    print(content)

