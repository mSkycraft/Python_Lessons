# HW 1
def weekend(a):
    a = a % 7
    if ((a==0)or(a==6)):
        return 'Да'
    return 'Нет'

try:
    enter = int(input('Введите целое число - '))
except:
    print('Не корректное значение')

print (f'День № {enter} выходной? - {weekend(enter)}')