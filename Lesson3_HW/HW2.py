sp = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe', '123', '234', '698', '567']

def Finder(sp,value):
    sum = 0
    for i in sp:
        count = 0
        j = -1
        while(j<len(i)):
            if i.find(value,j+1)==-1:
                break
            else:
                count = count + 1
                j = i.find(value,j+1)
        sum = sum + count
    if(sum== 0):
        return -1
    return sum


print(Finder(sp,'asdf'))