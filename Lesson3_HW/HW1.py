sp = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe', '123', '234', '698', '567']

def Find(sp:list,what):
    flag = False
    for i in sp:
        if(str(sp).find(what)!=-1):
            flag=True
    return flag

print(Find(sp,"54"))