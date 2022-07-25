import re

def readfile(name):
    f = open(name,'r')
    text =  f.read()
    f.close()
    print(text)
    return text

def summul(f1,f2):
    allmul = {}
    nonsums1 = re.findall(r"-?\d+x\^\d+",f1)
    for i in range(len(nonsums1)):
        nonsums1[i] = nonsums1[i].split('x^')
    for i in range(len(nonsums1)):
        allmul[nonsums1[i][1]] = int(nonsums1[i][0])
    nonsums2 = re.findall(r"-?\d+x\^\d+",f2)
    for i in range(len(nonsums2)):
        nonsums2[i] = nonsums2[i].split('x^')
    for i in range(len(nonsums2)):
        if(nonsums2[i][1] in allmul):
            allmul[nonsums2[i][1]] += int(nonsums2[i][0])
        else:
            allmul[nonsums2[i][1]] = int(nonsums2[i][0])
    result = ''
    for key,val in allmul.items():
        if(int(val)>0):
            result+="+" + str(val)+"x^"+key
        elif(int(val)<0):
            result+=str(val)+"x^"+key
    return result

mul1 = readfile("mn1.txt")
mul2 = readfile("mn2.txt")

result = summul(mul1,mul2)
print(result)
f = open("summul.txt",'w')
f.writelines(result)
f.close()