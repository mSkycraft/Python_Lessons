N = int(input('Введите число - '))

print('[ ', end='')
for j in range(1,N+1):
    pr = 1
    if (j!=1):
        print('', end=', ')
    for i in range(1,j+1):
        pr = pr * i
    print(pr, end='')
print(' ]')
