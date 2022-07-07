from math import sqrt


X = list(map(float,input('Введите координаты через запятую X - ').split()))
Y = list(map(float,input('Введите координаты через запятую Y - ').split()))
try:
    x1 = float(X[0])
    y1 = float(X[1])
    x2 = float(Y[0])
    y2 = float(Y[1])
except:
    print('Введены некорректные значения')


def len (a,b,c,d):
    return sqrt((c-a)**2+(d-b)**2)

print(f'Расстояние между двумя точками равно - {len(x1,y1,x2,y2)}')
