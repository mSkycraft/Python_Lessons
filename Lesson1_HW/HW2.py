# HW 2

def test(x,y,z):
    if not(x or y or z) == ((not(x)) and (not(y)) and (not(z))):
        return(True)
    else:
        return(False)
    
#print(test(True,False,False))

marker = True
for i in False,True:
    for j in False,True:
        for k in False,True:
            if(test(i,j,k)!=True):
                marker = False

print(marker)

print(test(True,False,True))
#Не очень понял что именно надо было подавать на вход