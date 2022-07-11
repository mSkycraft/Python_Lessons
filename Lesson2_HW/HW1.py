def summ (enter):
    cel = int(enter%10)
    print(f'{enter} : {cel}')
    if(enter==0): return 0
    else:
        return cel + summ(int(enter/10))


flo = float(input('Введите число - '))
flOr = flo
while(flo%1!=0):
    flo = flo*10
print(f'Сумма цифр числа {flOr} = {summ(flo)}')