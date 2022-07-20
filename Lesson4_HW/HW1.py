def div(a,b,d):
    if(d>=1): D = 0
    else: D = 1
    while(d*10<1):
        d = d*10
        D = D + 1

    print(D)
    return round(a/b,D)


d = 0.001

print(div(5,3,d))

print(div(5,3,1))