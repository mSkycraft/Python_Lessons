from audioop import mul
import random as rnd



def multi(k):
    asd = ''
    step = k
    for i in range(k+1):
        koof = round((rnd.random()-0.5)*100,0)
        if(step == 0):
            if(koof > 0):
                asd += '+'+ str(int(koof))
            elif(koof < 0):
                asd += str(int(koof))
        else:
            if(koof > 0):
                if(asd != ''):
                    asd += '+'+ str(int(koof)) + 'x^'+ str(step)
                else:
                    asd += str(int(koof)) + 'x^'+ str(step)
            elif(koof<0):
                asd += '-'+ str(abs(int(koof))) + 'x^'+ str(step)
        step = k - i -1
    
    asd += ' = 0'
    return asd

print(multi(5))
file = open("mn2.txt",'w')
file.write(multi(10))
file.close()