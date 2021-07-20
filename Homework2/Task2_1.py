import random
print('Приветствуем в вирутальном казино. На Вашем депозитном счете 10000')
list = []
i = 1
deposit = 10000
while deposit > 0:
    if deposit <= 0:
        print ('Депозит закончился')
    rnd_value = random.randint(2, 12)
    user_value = int(input('Угадайте сумму чисел на кубиках. Попытка №' + str(i) + ':'))
    i+=1
    if user_value < 2 or user_value > 12:
        print('Неверный ввод. Сумма кубиков не  может быть меньше 2 и больше 12')
        break
    if user_value == rnd_value:
        deposit += 1000
        print('Вы угадали число {}!'.format(rnd_value), 'Твой депозитный счет пополнен', deposit)
    else:
        print('На кубиках {}.'.format(rnd_value), 'А Вы загадали {}.'.format(user_value))
        deposit-=1000
        print('На твоем счету осталось', deposit)
    list.append(f'Загаданное число {user_value},загаданное программой число {rnd_value}, ваш остаточный счет {deposit}')
for element in list:
    print(element)
