# HW4

index = input('Введите номер четверти - ')

def test(a):
    if(a<=0 or 5<=a):
        print('Введены значения вне диапазона')
    else:
        match a:
            case 1: 
                print('0 < X < Ꚙ')
                print('0 < Y < Ꚙ')
            case 2: 
                print('-Ꚙ  < X < 0')
                print('0 < Y < Ꚙ')
            case 3: 
                print('-Ꚙ  < X < 0')
                print('-Ꚙ  < Y < 0')
            case 4: 
                print('0 < X < Ꚙ')
                print('-Ꚙ  < Y < 0')

try:
    index = int(index)
    test(index)
except:
    print('Введены некорректные значения')

