cat = 0
res = []
string_line = []

with open('Raskaz.txt', encoding='utf-8') as file:
    for line in file:
        for word in line.split():
            if word == 'кошка':
                cat+= 1
                string_line.append(line)

for i in string_line:
    if i not in string_line:
        string_line.append(i)

for i in string_line:
    print(i)


print(cat)

