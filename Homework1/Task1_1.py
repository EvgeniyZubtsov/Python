#Напишите программу, которая считает, сколько пользователю лет в том или ином году.
# Сначала программа спрашивает год рождения пользоватля,
# а затем , год, к которому нужно будет рассчитать возраст.
# После этого программа должна рассчитать возврат и вывести его на экран
Question = int(input("В каком году вы родились?: "))
Answer = int(input("К каком году нужно посчитать возраст: "))
Score = (Answer - Question)
def print_answer(Score):
    remainder = Score % 10
    if remainder  == 1 and remainder != 11:
        print (f'Ваш возраст в {Answer} будет {Score} год')
    elif (remainder >= 2 and remainder <= 4):
        print (f'Ваш возраст в {Answer} будет {Score} годa')
    else:
        print(f'Ваш возраст в {Answer} будет {Score} лет')

print_answer(Score)