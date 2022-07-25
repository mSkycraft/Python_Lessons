from itertools import chain, count
from math import fabs
from unittest import result


st = 'AAAAAAADDDDDDDDDDSBBBBBBEFAS'

def arh(ls):
    char = None
    count = 0
    result = ''
    for i in ls:
        if(count == 0):
            char = i
            count += 1
        elif(char == i):
            count += 1
        else:
            result += char + str(count)
            char = i
            count = 1
    result += char + str(count)
    return result

print(st)
print(arh(st))


def unarh(ls:list):
    char = None
    number = ''
    result = ''
    for i in range(len(ls)):
        if(ls[i].isnumeric() != True):
            char = ls[i]
        else:
            while(True):
                if(ls[i].isnumeric() == True):
                    number += ls[i]
                    if(i+1< len(ls)):
                        i += 1
                    else:
                        break
                else:
                    break
            
            if(number != ''):
                result += char * int(number)
            number = ''
    return result


print(unarh(arh(st)))
