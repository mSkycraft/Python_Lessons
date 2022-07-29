import numpy as np
import random as rnd
import os

map1 = np.zeros((3,3))
map1Result = np.zeros((3,3))
map2 = np.zeros((3,3))
map2Result = np.zeros((3,3))

def BotRndStart(mp):
    cordx = rnd.randrange(0,2)
    cordy = rnd.randrange(0,2)
    mp[cordx][cordy] = 1
    return mp

def PlayersetStart(mp):
    x = int(input("Введите x  =  "))
    y = int(input("Введите y  =  "))
    mp[x][y] = 1
    return mp

def PlayerAttack(mp,mpRes):
    x = int(input("Введите x  =  "))
    y = int(input("Введите y  =  "))
    if(mp[x][y]==1):
        mp[x][y]=0
        print("Player Win")
    mpRes[x][y] = 1
    return mp,mpRes

def BotAttack(mp,mpRes):
    full = True
    for i in range(len(mpRes)):
        for j in range(len(mpRes)):
            if(mpRes[i,j]!=1):    
                full = False

    while(full != True):
        cordx = rnd.randrange(0,2)
        cordy = rnd.randrange(0,2)
        if(mpRes[cordx][cordy]!=1):
            if(mp[cordx][cordy]== 1):
                mp[cordx][cordy] = 0
                print("Bot Win")
            mpRes[cordx][cordy] = 1
            return mp,mpRes


def CheckMap(mp):
    for i in range(len(mp)):
        for j in range(len(mp)):
            if(mp[i,j]==1):    
                return False
    return True

def PrintAll(map1,map2,map1Result,map2Result):
    print("Player map")
    PrintMap(map1,map1Result)
    print("Bot map")
    PrintMap(map2,map2Result)

def PrintMap(mp,mpRes):
    for i in range(len(mp)):
        print(mp[i],end='    ')
        print(mpRes[i])
    return True

map1 = PlayersetStart(map1)
map2 = BotRndStart(map2)


while(True):
    map2,map2Result = PlayerAttack(map2,map2Result)
    if(CheckMap(map2) == True):
        break
    map1,map1Result = BotAttack(map1,map1Result)
    if(CheckMap(map1) == True):
        break
    PrintAll(map1,map2,map1Result,map2Result)

print("Конечный результат")
PrintAll(map1,map2,map1Result,map2Result)