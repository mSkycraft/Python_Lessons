#обьекты 3 шт.
#их скорость
#старт собаки от 1го
#расстояние между ними
def steps(a,b,c,d):
    point = True
    time = 0
    count = 0
    sumtime = 0
    while(d>10):
        if(point == True):
            if(b<0):
                time = d/(c-b) #Собака догоняет
            else:
                time = d/(b+c) #Собака бежит на встречу
            if(time<=0):
                print('Собака не догонит 2го человека')
                break
            point = False
        else:
            if(a>0):
                time = d/(a+c)
            else:
                time = d/(c-a)
            if(time<=0):
                print('Собака не догонит 1го человека')
                break
            point = True
        d = d - (a+b)*time
        sumtime += time
        count = count + 1
        if(d>1000): 
            print(f'Собака пошлет всех нафиг, дистанция {round(d)}') 
            break
    return count,round(sumtime,2)


print(f'Результат {steps(1,4,5,100)}')
print(f'Результат {steps(-10,4,5,100)}')
print(f'Результат {steps(1,-4,5,100)}')
print(f'Результат {steps(-1,-4,5,100)}')
