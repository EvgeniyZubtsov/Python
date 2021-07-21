spisok = [0,1,2,3,4,5,6,7,8,9]
for i in range(1,len(spisok)):
    number1 = i
    for j in range(1,len(spisok)):
        number2 = j
        result = number1 * number2
        print(number1, '*', number2, '=', result)
    print('----------')