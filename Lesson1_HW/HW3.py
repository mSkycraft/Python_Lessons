# HW3

x = input('Введите X - ')
y = input('Введите Y - ')
try:
    x = float(x)
    y = float(y)
except:
    print('Введены некорректные значения')

def test(x,y):
    if (x>0 and y > 0):
        return 1
    elif (x>0 and y < 0):
        return 4
    elif (x<0 and y < 0):
        return 3
    else:
        return 2

if(x == 0 or y == 0):
        print('Одно из значений равно 0')
else:
    print(f'Координаты [{x},{y}] соответствуют четверти № - {test(x,y)}')

